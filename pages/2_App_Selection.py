import streamlit as st
from menu import render_menu
from style import inject_css

st.set_page_config(page_title="App Selection", layout="wide")
inject_css()

# Sidebar content (same across all pages)
with st.sidebar:
    st.markdown("### Shortcut Links")
    render_menu()
    st.image("static/teamlogo2.png", use_column_width=True)
    st.markdown("<div class='sidebar-footer'>Made for the CCMI Team</div>", unsafe_allow_html=True)

# Main content for App Selection
st.title("Select an Application")

app_details = {
    "MIRA": {
        "description": "MIRA is the main app for managing production.",
        "app_link": "https://mira-app.com",
        "dev_link": "https://dev.mira-app.com"
    },
    "CCMI Tracker": {
        "description": "This is the CCMI Tracker app.",
        "app_link": "https://ccmi-tracker.com",
        "dev_link": "https://dev.ccmi-tracker.com"
    },
    "Power BI Admin Center": {
        "description": "The admin center for Power BI management.",
        "app_link": "https://powerbi-admin.com",
        "dev_link": "https://dev.powerbi-admin.com"
    },
    "CCMI Request System": {
        "description": "Manage requests in the CCMI request system.",
        "app_link": "https://ccmi-request.com",
        "dev_link": "https://dev.ccmi-request.com"
    }
}

# Custom CSS for horizontal layout
st.markdown(
    """
    <style>
    .horizontal-select {
        display: flex;
        justify-content: space-between;
    }
    .horizontal-select div {
        padding: 10px;
        background-color: #2e2e2f;
        border-radius: 8px;
        margin-right: 10px;
        cursor: pointer;
        text-align: center;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Custom horizontal select box
app_selection = st.selectbox("Select an App:", list(app_details.keys()), key='app_selector')

# Use selected_app for app rendering
if app_selection:
    details = app_details[app_selection]
    st.write(f"### {app_selection}")
    st.write(details["description"])
    st.markdown(f'<iframe src="{details["app_link"]}" width="100%" height="500"></iframe>', unsafe_allow_html=True)
