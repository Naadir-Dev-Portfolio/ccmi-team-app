import streamlit as st

# Set up page configuration
st.set_page_config(page_title="CCMI Team Central Hub", layout="wide")

# Initialize session state for menu option and advanced option
if 'menu_option' not in st.session_state:
    st.session_state['menu_option'] = "Home"  # Default is Home
if 'advanced_option' not in st.session_state:
    st.session_state['advanced_option'] = None  # No advanced option selected by default

# List of menu options
menu_options_list = ["Home", "Power BI", "Power Apps", "SharePoint", "SAP", "Telephony", "Citrix", "Zohodesk"]

# Define the sidebar and logo image
with st.sidebar:
    st.image("static/teamlogo2.png", use_column_width=True)
    st.title("Navigation")

    # Sidebar options for main navigation (menu)
    selected_menu_option = st.radio(
        "Go to",
        menu_options_list,
        index=menu_options_list.index(st.session_state['menu_option'])
    )

    # Update session state immediately when the radio button changes
    if selected_menu_option != st.session_state['menu_option']:
        st.session_state['menu_option'] = selected_menu_option
        st.session_state['advanced_option'] = None

    # Advanced section with an expander
    with st.expander("Advanced"):
        st.write("Select one of the following advanced options:")

        # Power Query Code Option
        if st.button("Power Query Code"):
            st.session_state['advanced_option'] = "Power Query"

        # Excel Formulas Option
        if st.button("Excel Formulas"):
            st.session_state['advanced_option'] = "Excel Formulas"

        # VBA Code Option
        if st.button("VBA Code"):
            st.session_state['advanced_option'] = "VBA Code"

# Define logic to decide which content to show in the main content area

# If an advanced option is selected, prioritize that over the radio button menu
if st.session_state['advanced_option']:
    if st.session_state['advanced_option'] == "Power Query":
        st.title("Power Query Code")
        st.code("""
        let
            Source = Excel.Workbook(File.Contents("C:\\path\\to\\your\\file.xlsx"), null, true),
            Sheet1 = Source{[Name="Sheet1"]}[Data],
            #"Changed Type" = Table.TransformColumnTypes(Sheet1,{{"Column1", type text}, {"Column2", type number}})
        in
            #"Changed Type"
        """, language='powerquery')

    elif st.session_state['advanced_option'] == "Excel Formulas":
        st.title("Excel Formulas")
        st.code("""
        =IF(A1>10, "Greater than 10", "Less than or equal to 10")
        """, language='excel')

    elif st.session_state['advanced_option'] == "VBA Code":
        st.title("VBA Code")
        st.code("""
        Sub HelloWorld()
            MsgBox "Hello, World!"
        End Sub
        """, language='vba')

# If no advanced option is selected, show content based on the main menu (radio button)
else:
    if st.session_state['menu_option'] == "Home":
        st.title("Welcome to CCMI Team Central Hub")
        st.write("""
        This is the homepage for the CCMI Team. Use the navigation on the left to explore various sections including Power BI, Power Apps, SharePoint, SAP, and more. Each section provides quick access to key tools and resources for the team.
        """)

    elif st.session_state['menu_option'] == "Power BI":
        st.title("Power BI Section")
        st.write("Comprehensive links and resources for Power BI management.")

        # Create two columns for layout
        col1, col2 = st.columns(2)
        with col1:
            st.image("static/powerbi.png", width=100)
            st.subheader("Dataflow Warehouse")
            st.write("Link to the Dataflow Warehouse for Power BI.")
            st.markdown('<iframe src="https://app.powerbi.com/groups/eae3ff49-45b4-414b-888c-5238c738d787/list?experience=power-bi" width="100%" height="300"></iframe>', unsafe_allow_html=True)
            st.image("static/powerbi.png", width=100)
            st.subheader("Power BI Production")
            st.write("Link to the Power BI Production environment.")

        with col2:
            st.subheader("Example Embeds:")
            st.write("Embed iframe below:")
            st.markdown('<iframe src="https://app.powerbi.com/groups/me/apps/7c4d33b8-9dd7-4791-88af-fd0f770309ae/dashboards/59843adc-2aa1-4ccf-8" width="100%" height="300"></iframe>', unsafe_allow_html=True)
            st.subheader("Main Power BI App")
            st.write("Access the main Power BI App.")
            st.markdown('<iframe src="https://example.com" width="100%" height="300"></iframe>', unsafe_allow_html=True)

    elif st.session_state['menu_option'] == "Power Apps":
        st.title("Power Apps Section")
        st.write("Power Apps for managing internal and external team functions.")

        # Two-column layout with iframes
        col1, col2 = st.columns(2)
        with col1:
            st.image("static/powerapp.png", width=100)
            st.subheader("Power BI Admin Centre")
            st.write("Admin Centre for Power BI management.")
            st.markdown('<iframe src="https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/4ad6d92b-186f-4803-a836-e3a807ce2f59?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769" width="100%" height="300"></iframe>', unsafe_allow_html=True)
            st.subheader("Power BI Request App")
            st.write("Request app for Power BI services.")

        with col2:
            st.image("static/powerautomate.png", width=100)
            st.subheader("CCMI Workload Tracker")
            st.write("Workload tracker for CCMI.")
            st.markdown('<iframe src="https://apps.powerapps.com/play/e/b4016bdf-d476-4c6b-80f1-ab29055b8d71/a/a3622e39-c862-4064-a361-a89c327690b3?tenantId=de0d74aa-9914-4bb9-9235-fbefe83b1769" width="100%" height="300"></iframe>', unsafe_allow_html=True)
            st.subheader("CCMI Request App")
            st.write("App for requesting CCMI services.")

        # Example of embedded iframe for reference
        st.markdown('<iframe src="https://example.com" width="100%" height="300"></iframe>', unsafe_allow_html=True)

    elif st.session_state['menu_option'] == "SharePoint":
        st.title("SharePoint Section")
        st.image("static/sharepoint.png", width=100)
        st.write("Trackers and sites for SharePoint management.")

        st.subheader("SharePoint Sites")
        st.write("Access to various SharePoint sites including:")
        st.write("- CCMI Team Drive area")
        st.write("- Team 121 Packs area")

        st.subheader("SharePoint Trackers")
        st.write("Trackers used by the CCMI team:")
        st.write("- CCMI Requests")
        st.write("- Security Groups list")

    elif st.session_state['menu_option'] == "SAP":
        st.title("SAP Section")
        st.image("static/sap.png", width=100)
        st.write("Tools and resources for SAP management.")

        st.subheader("SAP Business Warehouse")
        st.write("Link to SAP Business Warehouse.")

        st.subheader("SAP UI5 (Unplanned Interruptions)")
        st.write("Manage unplanned interruptions with SAP UI5.")

        st.subheader("401 Unplanned Interruptions Data")
        st.write("Access to the 401 Unplanned Interruptions Data.")

        st.subheader("SAP CRM Password")
        st.write("Manage SAP CRM Passwords.")

    elif st.session_state['menu_option'] == "Telephony":
        st.title("Telephony Section")
        st.image("static/list.png", width=100)
        st.write("Access telephony-related systems for data extraction.")

        st.subheader("eGain")
        st.write("Link to eGain for call-related data.")

        st.subheader("Verint")
        st.write("Link to Verint for call-related data extraction.")

        st.subheader("AWS")
        st.write("Link to AWS for telephony services.")

    elif st.session_state['menu_option'] == "Citrix":
        st.title("Citrix Section")
        st.image("static/search.png", width=100)
        st.write("Access mapping and virtual machine tools via Citrix.")

        st.subheader("Arc Catalog")
        st.write("Link to Arc Catalog.")

        st.subheader("Esri Maps")
        st.write("Link to Esri Maps.")

        st.subheader("Virtual Machines")
        st.write("Link to virtual machines.")

    elif st.session_state['menu_option'] == "Zohodesk":
        st.title("Zohodesk Section")
        st.image("static/question.png", width=100)
        st.write("Manage communications through Zohodesk.")

    else:
        st.write("Please select an option from the navigation menu.")
