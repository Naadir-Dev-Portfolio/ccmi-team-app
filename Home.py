import streamlit as st
from menu import render_menu  # Import the JavaScript menu
from style import inject_css

st.set_page_config(page_title="Home", layout="wide")
inject_css()

# Sidebar content
with st.sidebar:
    st.markdown("### Shortcut Links")
    render_menu()
    st.image("static/teamlogo2.png", use_column_width=True)
    st.markdown("<div class='sidebar-footer'>Made for the CCMI Team</div>", unsafe_allow_html=True)

# Main content of homepage
st.title("Welcome to the CCMI Team Central Hub")
st.write("We are a dedicated team managing various tools like Power BI, SAP, and more.")
st.markdown('<iframe src="https://example.com" width="100%" height="400"></iframe>', unsafe_allow_html=True)
