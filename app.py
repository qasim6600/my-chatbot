import os
import gradio as gr

# Your app logic here — example demo app
def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Correct port handling for Azure and local
port = int(os.environ.get("PORT", 7860))

# Must bind to 0.0.0.0 for Azure
demo.launch(server_name="0.0.0.0", server_port=port)
