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

# Application details with description, app link, and dev link
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

# Application selection dropdown
app_selection = st.selectbox("Select an App:", list(app_details.keys()), key='app_selector')

# If an application is selected, display the app and dev version
if app_selection:
    details = app_details[app_selection]
    st.write(f"### {app_selection}")
    st.write(details["description"])

    # Main app section with external link and iframe
    st.markdown(f'''
        <a href="{details["app_link"]}" target="_blank">
            <button style="background-color:#2E2E2E; color:#FFFFFF; padding:8px 16px; border:none; border-radius:4px; cursor:pointer; font-size:14px; margin-bottom:15px;">
                Open {app_selection} Externally
            </button>
        </a>
    ''', unsafe_allow_html=True)
    st.markdown(f'<iframe src="{details["app_link"]}" width="100%" height="450"></iframe>', unsafe_allow_html=True)

    # Dev version section with expander
    with st.expander("Dev Version"):
        st.markdown(f'''
            <a href="{details["dev_link"]}" target="_blank">
                <button style="background-color:#2E2E2E; color:#FFFFFF; padding:8px 16px; border:none; border-radius:4px; cursor:pointer; font-size:14px; margin-bottom:15px;">
                    Open Dev Version
                </button>
            </a>
        ''', unsafe_allow_html=True)
        st.markdown(f'<iframe src="{details["dev_link"]}" width="100%" height="450"></iframe>', unsafe_allow_html=True)
