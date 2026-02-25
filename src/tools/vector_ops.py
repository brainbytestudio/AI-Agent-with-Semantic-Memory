import chromadb
from datetime import datetime
from agents import function_tool
from sentence_transformers import SentenceTransformer

# -------------------------------
# Local Embedding Model
# -------------------------------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# Chroma Persistent Store
# -------------------------------
client = chromadb.PersistentClient(path="./conversation_memory")
collection = client.get_or_create_collection(
    name="brainbyte_semantic_store"
)

@function_tool
def semantic_memory_search(query: str) -> dict:
    """
    Semantic (meaning-based) memory search.
    Returns structured results for agent reasoning.
    """
    query_vector = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=2
    )

    if not results["documents"][0]:
        return {"found": False}

    entries = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        entries.append({
            "content": doc,
            "timestamp": meta["timestamp"],
            "source": meta["source"]
        })

    return {
        "found": True,
        "entries": entries
    }


def add_to_semantic_memory(content: str, source: str):
    """
    Store CLEAN, synthesized knowledge only.
    """
    vector = embed_model.encode(content).tolist()
    ts = datetime.now().isoformat()

    collection.add(
        embeddings=[vector],
        documents=[content],
        metadatas=[{
            "timestamp": ts,
            "source": source
        }],
        ids=[f"id_{ts}_{source}"]
    )
