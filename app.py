from example_text import one_paragraph, one_page
from pricing import MODEL_CONFIG, calculate_cost
from utils import num_tokens_from_string, analyze_string
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="llm-token-calculator",
    page_icon="🧮",
    layout="wide"  # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

st.title("🧮 LLM Token Calculator - Text")

st.write("Pricing last updated: 2023-11-15")
st.write("Calculates the number of tokens and estimated cost for a given input/output text and LLM model.")
st.write("GitHub repo: https://github.com/Ecom-Analytics-Co/llm-token-calculator")
with st.expander("Sources"):
    st.markdown("""
    - https://openai.com/pricing
    - https://platform.openai.com/docs/models
    - https://www.anthropic.com/pricing
    """)


llm_model = st.selectbox("LLM Model", tuple(MODEL_CONFIG.keys()))

st.subheader("Input")

input_text = st.text_area("Sys + User Text", height=350)
# st.session_state.input_text = input_text

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

