## main.py
from gpt_model import MetaGPT
from gui import GradioInterface
from utils import handle_exception

class Main:
    def __init__(self, gui: GradioInterface, gpt_model: MetaGPT):
        self.gui = gui
        self.gpt_model = gpt_model

    @handle_exception
    def run(self):
        """
        Function to run the main application.
        """
        while True:
            # Get user input from the GUI
            input = self.gui.get_input()

            # Check if the input is not None or empty to break the loop
            if not input:
                break

            # Generate text using the GPT model
            output = self.gpt_model.generate_text(input)

            # Display the output in the GUI
            self.gui.display_output(output)

if __name__ == "__main__":
    # Initialize the GPT model
    gpt_model = MetaGPT()

    # Initialize the Gradio interface with the GPT model's generate_text function
    gui = GradioInterface(gpt_model.generate_text)

    # Create the Gradio interface
    interface = gui.create_interface()

    # Launch the Gradio interface
    interface.launch()

    # Initialize the main application
    main = Main(gui, gpt_model)

    # Run the main application
    main.run()
