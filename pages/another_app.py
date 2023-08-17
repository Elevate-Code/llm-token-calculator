import streamlit as st

st.set_page_config(
    page_title="Streamlit Pages Demo",
    page_icon="🤖",
    layout="centered" # "centered" constrains page content to a fixed width; "wide" uses the entire screen
)

st.title("📃 This is how you add other pages")

st.write("""More info here: [Get started > Multipage apps](https://docs.streamlit.io/library/get-started/multipage-apps)""")


st.write("""Note that `st.session_state` persists across pages, so you can use it to share data between pages.""")
if 'count' not in st.session_state:
    st.session_state.count = 0
plus_one_btn_clicked = st.button('Add +1')
if plus_one_btn_clicked:
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)