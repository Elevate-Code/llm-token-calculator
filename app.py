import streamlit as st
from dotenv import load_dotenv
import tiktoken

load_dotenv()


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

st.set_page_config(
    page_title="llm-token-calculator",
    page_icon="🧮",
    layout="centered" # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

st.title("🧮 LLM Token Calculator")

