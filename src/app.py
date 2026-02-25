import gradio as gr
from agents import Runner
from phoenix.otel import register

from my_agents import memory_chatbot
from tools.vector_ops import add_to_semantic_memory

# ----------------------------------
# Phoenix auto-instrumentation ONLY
# ----------------------------------
register(
    project_name="BrainByte-Semantic-Memory",
    auto_instrument=True
)


async def chat_function(message, history):
    # -------------------------------
    # Flatten Gradio 6.x history
    # -------------------------------
    agent_input = []

    for msg in history or []:
        role = "user" if msg["role"] == "user" else "assistant"
        content = msg["content"]

        if isinstance(content, list):
            text = " ".join(
                item.get("text", "")
                for item in content
                if isinstance(item, dict)
            )
        else:
            text = str(content)

        agent_input.append({"role": role, "content": text})

    current_text = message if isinstance(message, str) else message.get("text", "")
    agent_input.append({"role": "user", "content": current_text})

    # -------------------------------
    # Run agent
    # -------------------------------
    try:
        result = await Runner.run(memory_chatbot, input=agent_input)
        output_text = result.final_output or "Response generated."

        # -------------------------------
        # Persist clean semantic knowledge
        # -------------------------------
        add_to_semantic_memory(output_text, source="knowledge")

        return output_text

    except Exception as e:
        return f"⚠️ Error occurred: {str(e)}"


with gr.Blocks() as demo:
    gr.Markdown(
        "# 🧠 BrainByte — Semantic Memory AI Agent\n"
        "*Local tracing powered by Arize Phoenix (auto-instrumentation)*"
    )
    gr.ChatInterface(chat_function)

if __name__ == "__main__":
    demo.launch()
