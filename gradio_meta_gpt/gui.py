import gradio as gr
from typing import Callable

class GradioInterface:
    def __init__(self, function: Callable[[str], str]):
        self.function = function

    def create_interface(self):
        """
        Function to create the Gradio interface.
        """
        interface = gr.Interface(fn=self.function,
                                 inputs=gr.inputs.Textbox(lines=5, placeholder="Enter text here..."),
                                 outputs="text")
        return interface

    def display_output(self, output: str):
        """
        Function to display the output in the Gradio interface.
        Args:
            output (str): The output string.
        """
        print(output)
