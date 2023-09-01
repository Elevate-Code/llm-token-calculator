import tiktoken
import re


def num_tokens_from_string(string: str, model_name: str) -> int:
    """
    Returns the number of tokens in a text string for a given model.
    See list of supported models here:
    https://github.com/openai/tiktoken/blob/main/tiktoken/model.py
    """
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def analyze_string(s):
    # Number of characters (excluding spaces)
    num_characters = len(s.replace(' ', ''))
    # Number of words
    words = s.split()
    num_words = len(words)
    # Number of proper sentences
    # This uses a regular expression to count occurrences of patterns that typically end sentences: . ! ?
    # Note that this will not work for text that contains non-standard sentence endings
    num_sentences = len(re.findall(r"[.!?]", s))
    return num_characters, num_words, num_sentences
