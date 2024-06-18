import gradio as gr
import numpy as np

def reverse_audio_fn(audio):
    sr, data = audio
    reversed_audio = (sr,np.flipud(data))
    return reversed_audio


mic = gr.Audio(sources = 'microphone', type='numpy', label= 'speak here')

demo = gr.Interface(reverse_audio_fn, mic,"audio",)

