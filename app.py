import gradio as gr
from fastapi import FastAPI
import uvicorn
import os

# Your Gradio logic
def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Wrap with FastAPI
app = FastAPI()
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))  # Ensure it's set to 80 for Azure
    uvicorn.run(app, host="0.0.0.0", port=port)
