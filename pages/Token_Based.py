from example_text import one_paragraph, one_page
from pricing import MODEL_CONFIG, calculate_cost
from utils import num_tokens_from_string, analyze_string
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="llm-token-calculator",
    page_icon="🧮",
    layout="wide"  # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

st.title("🧮 LLM Token Calculator - Tokens")


in_tokens = st.number_input("Input Tokens", value=1000)
out_tokens = st.number_input("Output Tokens", value=800)

options = st.multiselect(
    'Price compare these models',
    options=['gpt-4-1106-preview', 'gpt-4-1106-vision-preview', 'gpt-4', 'gpt-4-32k', 'gpt-3.5-turbo-1106',
     'text-davinci-003', 'text-embedding-ada-002', 'ft:gpt-3.5-turbo', 'claude-2', 'claude-instant'],
    default=['gpt-4-1106-preview', 'gpt-4', 'gpt-3.5-turbo-1106', 'ft:gpt-3.5-turbo', 'claude-2', 'claude-instant']
)

# calculate the totals and cost for each selected model into a table
results_table = []
results_table_columns=['Model', 'Total Tokens', 'Max Tokens', '% of Max Tokens', 'Total Cost']
for llm_model in options:
    model_max_tokens = MODEL_CONFIG[llm_model]['max_tokens']
    total_cost = calculate_cost(llm_model, in_tokens, out_tokens)
    total_tokens = in_tokens + out_tokens
    percentage_of_max = total_tokens / model_max_tokens * 100
    results_table.append([
        llm_model, total_tokens, model_max_tokens, percentage_of_max, total_cost
    ])

# create pandas dataframe to display results
df = pd.DataFrame(results_table, columns=results_table_columns)
df = df.set_index('Model')
df['% of Max Tokens'] = df['% of Max Tokens'].apply(lambda x: "{:.0f}%".format(x))
df['Total Cost'] = df['Total Cost'].apply(lambda value: "${:,.3f}".format(value))
st.dataframe(df)

