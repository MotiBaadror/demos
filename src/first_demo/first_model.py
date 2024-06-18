import gradio as gr



def greet(name):
    return 'Hii '+name


demo = gr.Interface(fn = greet, inputs = 'text', outputs ='text')

