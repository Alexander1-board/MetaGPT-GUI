## gpt_model.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from typing import Optional
from utils import load_model, handle_exception

class MetaGPT:
    def __init__(self, model_name: str = "gpt2"):
        self.model, self.tokenizer = load_model(model_name)
        if self.model is None or self.tokenizer is None:
            raise Exception("Error in loading the model or tokenizer")

    @handle_exception
    def generate_text(self, input: str) -> Optional[str]:
        """
        Function to generate text using the GPT2 model.
        Args:
            input (str): The input string.
        Returns:
            output (str): The generated text.
        """
        inputs = self.tokenizer.encode(input, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=500, do_sample=True)
        output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return output
