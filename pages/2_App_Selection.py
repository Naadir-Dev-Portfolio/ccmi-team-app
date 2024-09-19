import streamlit as st
from menu import render_menu_1, render_menu_2 
from style import inject_css
from datetime import datetime

st.set_page_config(page_title="CCMI Production Apps", layout="wide")
inject_css()

# Sidebar content (same across all pages)
with st.sidebar:
    st.markdown("### Shortcut Links")
    render_menu_1()
    render_menu_2()
    # Create a column layout to center the image
    col1, col2, col3 = st.columns([1, 2, 1])  # 3 columns, with the middle one being wider to hold the image
    
    with col2:  # Place the image in the center column
        st.image("static/CCMI-systems-portrait3.png")  # Adjust the width as needed
        st.markdown("<div class='sidebar-footer'>Made for the CCMI Team</div>", unsafe_allow_html=True)

# Main content for App Selection
st.title("CCMI Power Apps")

########################################

col1, col2 = st.columns([1, 9])  # Adjust the ratio for better alignment

# Display the image in the first column
with col1:
    st.image("static/powerapp.png", width=65)  # Adjust the width of the image

# Display the title in the second column, aligned with the image
with col2:
    st.markdown("<h2 style='margin-top: 0px;'>Select an Application</h2>", unsafe_allow_html=True)

########################################

# Application details with description, app link, and dev link
app_details = {
    "MIRA": {
        "description": "MIRA is the main app for managing production.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/4ad6d92b-186f-4803-a836-e3a807ce2f59?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=39868a9f-e5f1-4c3a-9a0e-aab7403fdfce&sourcetime=1726586745986",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/1d281a67-d580-47cb-82a8-704f3fe80167?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=e77e3ec8-28ed-4d4a-924f-e08a6becfc34&sourcetime=1726587099190"
    },
    "CCMI Workload Tracker": {
        "description": "(Previously the SOP Tracker) - This app contains all CCMI Activities.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/a3622e39-c862-4064-a361-a89c327690b3?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=9cdc01b8-d7f0-48ec-ba28-fb6817bb8c34&sourcetime=1726586726518",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/33fa6d3b-a380-4e5e-8c3e-27483977f5f3?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=33fcde0a-1fbd-4c6d-9512-4c0a3575a46e&sourcetime=1726587111202"
    },
    "Power BI Admin Center": {
        "description": "The admin center for Power BI management (fault/change requests).",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/0a8ca27a-182d-4ea9-b75b-79d55114db42?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&sourcetime=1726586625911",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/d906e82b-8b74-42a5-b27f-ff6faebb0ac9?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&sourcetime=1726587016052"
    },
    "CCMI System Centre": {
        "description": "The System Centre is used to track all apps and systems managed by the CCMI Team.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/24eb788d-20a0-4979-9da0-16c7517577d5?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&sourcetime=1726586921242",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/2f2a0dea-1989-49aa-99e1-db358869c346?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&sourcetime=1726587077965"
    },
    "CCMI Request System - End user app": {
        "description": "This app allows users to raise change requests and new power app builds.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/41865c1b-58d9-4269-bba2-27e086716a73?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=0478a1ca-fdb6-4e36-a459-65b56088409e&sourcetime=1726586674423",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/4e752347-7f91-440c-9d2a-5f8f67d4279a?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=746834ba-9c2d-4a39-b9af-68c28f719e9f&sourcetime=1726587179355"
    },
    "Power BI Request System - End user app": {
        "description": "This app allows users to raise change request/faults and access to Power BI reports.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/005931a2-eb63-4533-aaa4-85908ec308fd?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=988680fd-c3c1-4333-b315-21eb0c55ff62&sourcetime=1726586859603",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/877d10c8-a067-491b-b334-03c47b7602c9?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=2e745ae8-261c-405d-891a-86e5b5185d08&sourcetime=1726587129586"
    },
    "Power BI Build Tracker": {
        "description": "For tracking and managing new Power BI Builds.",
        "app_link": "https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/3db21a54-2c6a-493e-8083-8b20e247822c?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=51c11250-c503-4205-b523-fbbc94515598&sourcetime=1726586892008",
        "dev_link": "https://apps.powerapps.com/play/e/6445976a-1b1e-e300-9696-9de0fccd64ae/a/e68dfe54-f6ef-4cd7-9ced-2612b425e91c?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769&hint=7e543c2a-c3fe-4800-8078-15203121626d&sourcetime=1726587214163"
    }
}

# Application selection dropdown
app_selection = st.selectbox("Select from the dropdown menu:", list(app_details.keys()), key='app_selector')

# If an application is selected, display the app and dev version
if app_selection:
    details = app_details[app_selection]
    st.write(details["description"])  # Display the app description

    # Two columns for the main app buttons (Open Externally & Refresh)
    col1, col2 = st.columns([1, 1])  # Adjusted the columns to be more narrow to bring buttons closer

    button_style = """
        background-color:#2E2E2E;
        color:#FFFFFF;
        padding:8px 16px;
        border:none;
        border-radius:4px;
        cursor:pointer;
        font-size:14px;
        margin-bottom:15px; /* Add space below the buttons */
    """

    # Left-align Open Externally button
    with col1:
        st.markdown(f'''
            <a href="{details['app_link']}" target="_blank">
                <button style="{button_style};">
                    Open {app_selection} Externally
                </button>
            </a>
        ''', unsafe_allow_html=True)

    # Right-align Refresh button
    with col2:
        st.markdown(f'''
            <div style="text-align:right;">
                <button onClick="window.location.reload();" style="{button_style};">
                    🔁 Refresh
                </button>
            </div>
        ''', unsafe_allow_html=True)

    # Main app iframe
    st.markdown(f'<iframe src="{details["app_link"]}" width="100%" height="450"></iframe>', unsafe_allow_html=True)

    # Dev version section with expander
    with st.expander("For Power Apps Admin - Dev Version"):
        st.write(f"### Dev Version: {app_selection}")

        # Two columns for the dev version buttons (Open Externally & Refresh)
        col1, col2 = st.columns([1, 1])  # Same adjustment for dev version buttons

        # Left-align Open Dev Externally button
        with col1:
            st.markdown(f'''
                <a href="{details['dev_link']}" target="_blank">
                    <button style="{button_style};">
                        Open Dev Version
                    </button>
                </a>
            ''', unsafe_allow_html=True)

        # Right-align Refresh Dev button
        with col2:
            st.markdown(f'''
                <div style="text-align:right;">
                    <button onClick="window.location.reload();" style="{button_style};">
                        🔁 Refresh
                    </button>
                </div>
            ''', unsafe_allow_html=True)

        # Dev app iframe
        st.markdown(f'<iframe src="{details["dev_link"]}" width="100%" height="450"></iframe>', unsafe_allow_html=True)

########################################

# Add the CCMI Team image at the bottom of the page and resize it
st.markdown("<br><br>", unsafe_allow_html=True)  # Add some space before the image


# Add the professional text before the banner
st.markdown("""
    <p style="text-align: center; font-size: 18px; line-height: 1.6;">
    The applications featured on this page are integral tools used by our team to streamline production and administrative tasks. 
    From managing Power BI reports and request systems to accessing SharePoint for collaboration, these apps support our daily operations efficiently. 
    The core applications enable us to track every activity, report, and workflow, ensuring we stay on top of our production work stack for the day. 
    Whether it's monitoring progress, managing data, or executing critical tasks, these apps are designed to help us stay organized and productive.
    </p>
    """, unsafe_allow_html=True)

# Then the banner image
# Center the image using Streamlit's columns
col1, col2, col3 = st.columns([1, 2, 1])  # This creates 3 columns, with the center column being twice as wide

with col2:
    st.image("static/banner.png")  # Place the image in the center column and adjust the width as needed
    current_year = datetime.now().year
    # Add the current year to the sidebar footer
    st.markdown(f"<div class='sidebar-footer'>Made for the CCMI Team - {current_year}</div>", unsafe_allow_html=True)
