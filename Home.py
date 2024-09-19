import streamlit as st
from menu import render_menu_1, render_menu_2  # Import the JavaScript menu
from style import inject_css
from datetime import datetime

st.set_page_config(page_title="Home", layout="wide")

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

# Main header content
st.image("static/teamlogo3.png", width=500)

# Function to get the current date
def get_current_time():
    now = datetime.now()
    return now.strftime("%A %d %B %Y")  # Example: "Monday 14 November 2024"

# Display current date under the title
st.markdown("<h1 style='text-align: center;'>Welcome to the Unofficial CCMI Homepage</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 30px; font-weight: bold; color: white; text-align: center;'>{get_current_time()}</p>", unsafe_allow_html=True)



# Summary sentence after the date
st.markdown(
    """
    <p style='font-size: 18px; line-height: 1.6; text-align: center;'>
        We are a specialized MI/BI Systems & Data team focused on optimizing business processes through data-driven insights. 
        <a href='https://cadentgasltd.sharepoint.com/' target='_blank' style='color: #00c0f0;'>Visit our SharePoint site</a> 
        to explore more about how we streamline operations.
    </p>
    """,
    unsafe_allow_html=True
)


# Break
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)  # This reduces the gap
 
# First section (Power BI)
col1, col2 = st.columns([1, 1])

with col1:
    st.image("static/pbhome.jpg")

with col2:
    st.image("static/adminctr.jpg")  # Set the width and height as needed


# Break
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)  # This reduces the gap


# Second section (Power Apps)
col1, col2 = st.columns([1, 1])

with col1:
    with st.expander("Learn more"):
        st.markdown(
        """
        <p style='font-size: 18px; line-height: 1.6;'>
            Our team leverages <a href='https://app.powerbi.com/' target='_blank' style='color: #00c0f0;'>Power BI</a> 
            to deliver comprehensive data visualizations and reporting solutions that drive informed decision-making. We design, 
            develop, and maintain numerous Power BI dashboards to ensure our stakeholders have easy access to real-time data, analytics, 
            and trends across various departments. By integrating multiple data sources, we help automate reporting processes, allowing our 
            organization to stay agile and data-driven.
        </p>
        """, 
        unsafe_allow_html=True
    )

with col2:
    with st.expander("Learn more"):
        st.markdown(
        """
        <p style='font-size: 18px; line-height: 1.6;'>
        In addition to Power BI, we play a critical role in automating workflows and processes through Power Apps. We build and manage 
        custom business apps that streamline various operational tasks, such as request systems, project tracking, and approvals. 
        Power Apps allow us to create tailored solutions quickly, helping teams reduce manual effort and focus on higher-value tasks.
        </p>
        """, 
        unsafe_allow_html=True
    )


# Final sentence for navigation
st.markdown(
    """
    <br><br>
    <p style='font-size: 18px; line-height: 1.6; color: white; text-align: center;'>
    Please use the links in the sidebar to navigate around our production system.
    </p>
    """, 
    unsafe_allow_html=True
)


# Footer section with centered banner and year
col1, col2, col3 = st.columns([1, 2, 1])  # 3 columns with the center one being wider

with col2:
    st.image("static/banner.png")  # Centered banner image
    current_year = datetime.now().year
    st.markdown(f"<div class='sidebar-footer'>Made for the CCMI Team - {current_year}</div>", unsafe_allow_html=True)
