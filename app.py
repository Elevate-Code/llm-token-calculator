import streamlit as st
import openai
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(
    page_title="Streamlit OpenAI Completion",
    page_icon="🤖",
    layout="wide" # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

def generate_response(message_placeholder):
    # note that you cant initialize widgets in functions
    response_content = ""
    for response in openai.ChatCompletion.create(
            model=model,
            stream=True,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ]
    ):
        response_content += response.choices[0].delta.get("content", "")
        message_placeholder.write(response_content + "▌")
    return response_content

st.title("🤖 Streamlit OpenAI Chat Completion Demo")

st.info("""
Streamlit reruns your script from top to bottom every time you interact with your app.

Assigning the current state of the widgets (checkbox, text fields, etc.) to a variable in the process.

Remember that each reruns takes place in a blank slate: no variables are passed between runs.

`st.session_state` is a special variable that persists across reruns of your script.

It is a dictionary that is initialized once when your script is first run, and can be accessed, updated, 
and cleared across reruns.
""", icon="ℹ️")


system_message = st.text_area('System Prompt', "You are a helpful assistant.")
user_prompt = st.text_area('User Prompt', placeholder="Enter a user message here.")

with st.expander("⚙️ Options", expanded=True):
    model = st.radio("Model", ('gpt-3.5-turbo', 'gpt-4'), index=1, horizontal=True)
    max_tokens = st.number_input("Max Tokens", 500)
    temperature = st.number_input("Temperature", 0.8)

send_btn_clicked = st.button("Send ➡️")
if send_btn_clicked:
    st.session_state['show_assistant_response'] = True

if 'show_assistant_response' in st.session_state: # hiding the assistant response section until send button clicked
    with st.expander("Assistant Response", expanded=True):
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            if send_btn_clicked:
                # Send new request & stream response when the send button is clicked...
                response_content = generate_response(message_placeholder)
                st.session_state['response_content'] = response_content
            else:
                #...and persist the response when other actions cause the script to rerun
                message_placeholder.write(st.session_state['response_content'])


st.divider()

st.write("Another example of using session state to persist variables across reruns:")
if 'count' not in st.session_state:
    st.session_state.count = 0
plus_one_btn_clicked = st.button('Add +1')
if plus_one_btn_clicked:
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)