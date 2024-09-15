# style.py
import streamlit as st

def inject_css():
    st.markdown(
        """
        <style>
        /* Your custom CSS styles */
        /* Sidebar background and text colors with compact design */
        [data-testid="stSidebarNav"] {
            background-color: #1c1c1e;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            margin-bottom: 10px;
        }

        /* Custom Title Styling for smaller size */
        .custom-title {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 10px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Smaller navigation links (Sidebar) */
        [data-testid="stSidebarNav"] a {
            font-size: 14px;
            color: #ffffff;
            padding: 8px 10px;
            text-decoration: none;
            border-radius: 6px;
            display: block;
            margin-bottom: 4px;
            background-color: #2c2c2e;
            transition: background-color 0.2s, transform 0.2s;
        }

        /* Hover effect for links with smaller adjustments */
        [data-testid="stSidebarNav"] a:hover {
            background-color: #3a3a3d;
            transform: translateX(3px);
        }

        /* Highlight the selected item */
        [data-testid="stSidebarNav"] a[aria-selected="true"] {
            background-color: #ff8800;
            color: #000;
        }

        /* Footer with smaller size */
        .sidebar-footer {
            color: #ffffff;
            font-size: 12px;
            text-align: center;
            margin-top: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Smaller centered logo with margin */
        [data-testid="stSidebar"] > div:first-child img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 15px;
            width: 120px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def set_horizontal_radio_button_style():
    st.markdown(
        """
        <style>
        /* Custom CSS to make specific radio buttons horizontal */
        div[data-baseweb="radio"] {
            display: flex;
            flex-direction: row;
        }
        div[data-baseweb="radio"] > label {
            margin-right: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )