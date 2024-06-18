from transformers import pipeline
import gradio as gr


model = pipeline('text-generation')

def predict(prompt):
    completion = model(prompt)[0]['generated_text']
    return completion


demo = gr.Interface(fn = predict, inputs="text", outputs='text')

