from example_text import one_paragraph, one_page
from utils import num_tokens_from_string, analyze_string
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="llm-token-calculator",
    page_icon="🧮",
    layout="wide"  # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

st.title("🧮 LLM Token Calculator")

st.write("Calculates the number of tokens and estimated cost for a given input/output text and LLM model.")

MODEL_CONFIG = {
    # pricing format is like this: (input_cost_per_token, output_cost_per_token),
    # OpenAI pricing: https://openai.com/pricing
    'gpt-3.5-turbo': {'max_tokens': 4097, 'pricing': (0.0015 / 1000, 0.002 / 1000)},
    'gpt-3.5-turbo-16k': {'max_tokens': 16384, 'pricing': (0.003 / 1000, 0.004 / 1000)},
    'gpt-4': {'max_tokens': 8192, 'pricing': (0.03 / 1000, 0.06 / 1000)},
    'gpt-4-32k': {'max_tokens': 32768, 'pricing': (0.06 / 1000, 0.12 / 1000)},
    'text-embedding-ada-002': {'max_tokens': 4097, 'pricing': (0.0001 / 1000, 0 / 1000)},
    'text-davinci-003': {'max_tokens': 4097, 'pricing': (0.02 / 1000, 0.02 / 1000)},
    # OpenAI finetuned models
    # training is 0.008 / 1000 tokens as of 09-2023 but not accounted for here
    'ft:gpt-3.5-turbo': {'max_tokens': 4097, 'pricing': (0.012 / 1000, 0.016 / 1000)},
    # Anthropic pricing: https://www.anthropic.com/pricing
    'claude-2': {'max_tokens': 100000, 'pricing': (11.02 / 1000000, 32.68 / 1000000)},
    'claude-instant': {'max_tokens': 100000, 'pricing': (1.63 / 1000000, 5.51 / 1000000)},
}


def calculate_cost(model_name, in_tokens, out_tokens):
    if model_name not in MODEL_CONFIG:
        raise ValueError("Unknown model name")
    input_cost_per_token, output_cost_per_token = MODEL_CONFIG[model_name]['pricing']
    total_request_cost = in_tokens * input_cost_per_token + out_tokens * output_cost_per_token
    return total_request_cost


llm_model = st.selectbox("LLM Model", tuple(MODEL_CONFIG.keys()))

st.subheader("Input")

col1, col2 = st.columns(2)
with col1:
    title, text = one_paragraph()
    if st.button(title):
        st.session_state.input_text = text
with col2:
    title, text = one_page()
    if st.button(title):
        st.session_state.input_text = text

# Initialize session_state if it's not set
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

input_text = st.text_area("Sys + User Text", value=st.session_state.input_text, height=350)
st.session_state.input_text = input_text

if llm_model in ['claude-2', 'claude-instant']:
    # claude *maybe* uses same token encoder as GPT-4: `cl100k_base`
    # https://www.linkedin.com/posts/zhenwang_anthropic-claude-tokenizer-activity-7067072872019619840-hZ-7/
    in_tokens = num_tokens_from_string(input_text, 'gpt-4')
if llm_model in ['ft:gpt-3.5-turbo']:
    # hacky way to accommodate finetuned models
    in_tokens = num_tokens_from_string(input_text, 'gpt-3.5-turbo')
else:
    in_tokens = num_tokens_from_string(input_text, llm_model)

# calculate string stats
char_count, word_count, sentence_count = analyze_string(input_text)
st.write(f"Characters: {char_count} || Words: {word_count} || Proper Sentences: {sentence_count}")

# calculate tokens
model_max_tokens = MODEL_CONFIG[llm_model]['max_tokens']
in_cost = calculate_cost(llm_model, in_tokens, out_tokens=0)
st.write(f"**{in_tokens}** request tokens ({in_tokens / model_max_tokens * 100:.0f}% of {model_max_tokens} max) || **Cost:** ${in_cost:,.4f}")


st.subheader("Output")

out_tokens = st.number_input("Plus Estimated Response Tokens", value=800)

st.subheader("Total")

total_cost = calculate_cost(llm_model, in_tokens, out_tokens)
st.write(f":orange[**Total Request Cost:**] ${total_cost:,.4f}")
total_tokens = in_tokens + out_tokens
percentage = total_tokens / model_max_tokens * 100
if percentage > 100:
    st.markdown(f"**{total_tokens}** request tokens (**:red[{percentage:.0f}%]** of {model_max_tokens} max)")
    st.write(":red[**Warning:**] This request will exceed the maximum number of tokens allowed for this model.")
else:
    st.write(f"**{total_tokens}** request tokens ({percentage:.0f}% of {model_max_tokens} max)")

