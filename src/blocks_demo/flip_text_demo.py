import gradio as gr


demo = gr.Blocks()

def flip_text(text):
    return text[::-1]


with demo:
    gr.Markdown(
        """
        #Flip Text 
        Start Typing Bwlow to see 
        """
    )
    with gr.TabItem('Flip Text'):
        with gr.Row():
            text_inputs = gr.Textbox(label='input text')
            text_outputs = gr.Textbox(label = 'Output_text')
            text_button = gr.Button('Flip Text')

    text_button.click(fn = flip_text, inputs= text_inputs,outputs=text_outputs)


    # inputs = gr.Textbox(placeholder='Input Text Here')
    # outputs = gr.Textbox()
    # inputs.change(fn = flip_text,inputs= inputs, outputs= outputs)



