import streamlit as st
from menu import render_menu
from style import inject_css

import google.generativeai as genai


st.set_page_config(page_title="CCMI AI Assistant", layout="wide")
inject_css()
# Sidebar content (same across all pages)
with st.sidebar:
    st.markdown("### Shortcut Links")
    render_menu()
    st.image("static/teamlogo2.png", use_column_width=True)
    st.markdown("<div class='sidebar-footer'>Made for the CCMI Team</div>", unsafe_allow_html=True)

# Main content for CCMI Assistant
st.title("CCMI AI Assistant")
st.write("Disclaimer: This is a work in an experimental feature. You will need to obtain an API key from Google to use the assistant.")

if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ''

if not st.session_state['api_key']:
    with st.form(key='api_key_form'):
        api_key = st.text_input("Please enter your Google API Key:", type="password")
        submit_api_key = st.form_submit_button("Submit API Key")
        if submit_api_key and api_key:
            try:
                genai.configure(api_key=api_key)
                st.session_state['api_key'] = api_key
                st.success("API key accepted! You can now use the assistant.")
            except Exception as e:
                st.error(f"Invalid API key or error: {e}")
else:
    with st.form(key='assistant_form'):
        user_query = st.text_input("Ask your question about ML, Data, or AI:")
        submit_query = st.form_submit_button("Ask")
        if submit_query and user_query:
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"You are a helpful ML and Data bot assistant. Answer the following user query: {user_query}"
                response = model.generate_content(prompt)
                st.write(f"**Answer:** {response.text}")
            except Exception as e:
                st.error(f"Error generating response: {e}")
