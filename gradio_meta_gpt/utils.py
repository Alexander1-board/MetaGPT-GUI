"""utils.py"""

from typing import Any, Tuple
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_model(model_name: str = "gpt2") -> Tuple[Any, Any]:
    """
    Function to load the GPT2 model and tokenizer.
    Args:
        model_name (str): The name of the model to be loaded. Default is "gpt2".
    Returns:
        model: The loaded model.
        tokenizer: The loaded tokenizer.
    """
    try:
        model = GPT2LMHeadModel.from_pretrained(model_name)
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        logger.error(f"Error in loading the model: {e}")
        return None, None

def handle_exception(func):
    """
    Decorator function to handle exceptions.
    Args:
        func (function): The function to be decorated.
    Returns:
        wrapper: The decorated function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper
