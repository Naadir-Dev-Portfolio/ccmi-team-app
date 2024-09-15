import streamlit.components.v1 as components

def render_menu():
    menu_html = """
    <style>
        /* Global styles */
        body, .menu-section, .sub-menu a {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Use modern fonts to match the app */
        }

        /* Main collapsible sections */
        .menu-section {
            cursor: pointer;
            font-size: 14px; /* Slightly smaller font to match sidebar */
            margin: 2px 0;  /* Tighten vertical margins */
            padding: 8px;  /* Adjust padding for internal spacing */
            background-color: #2c2c2e; /* Dark background to match sidebar */
            color: #ffffff; /* White text */
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.3s ease;
        }

        /* Hover effect for main sections */
        .menu-section:hover {
            background-color: #3a3a3d; /* Slightly lighter hover effect */
        }

        /* Sub-menu styling (hidden by default) */
        .sub-menu {
            display: none;
            margin-left: 15px;
            font-size: 13px; /* Slightly smaller font for sub-menu */
            color: #b3b3b3; /* Lighter text for sub-menu */
        }

        /* Links within the sub-menu */
        .sub-menu a {
            display: block;
            padding: 6px 10px;
            color: #ffffff; /* White text for sub-menu links */
            background-color: #2e2e2f; /* Darker background for sub-menu links */
            margin: 2px 0;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.2s;
        }

        /* Hover effect for sub-menu links */
        .sub-menu a:hover {
            background-color: #3a3a3d; /* Slightly lighter hover on submenu */
            color: #ffffff; /* Keep text white */
        }

        /* Toggle icon (plus/minus) */
        .icon {
            font-size: 16px;
            color: #ffffff; /* White for icons */
        }

        /* Scrollbar styling for sub-menu */
        .sub-menu {
            scrollbar-width: thin;
            scrollbar-color: #606274 #2e2e2f;
        }

        .sub-menu::-webkit-scrollbar {
            width: 6px;
        }

        .sub-menu::-webkit-scrollbar-track {
            background: #2e2e2f;
            border-radius: 3px;
        }

        .sub-menu::-webkit-scrollbar-thumb {
            background-color: #606274;
            border-radius: 3px;
            border: 1px solid #2e2e2f;
        }

        .sub-menu::-webkit-scrollbar-thumb:hover {
            background-color: #7a7c8e;
        }

        /* Make sub-menus scrollable */
        .sub-menu {
            max-height: 150px;
            overflow-y: auto;
        }
    </style>

    <script>
        // JavaScript function to toggle visibility of sub-menus
        function toggleMenu(menuId) {
            var menu = document.getElementById(menuId);
            var icon = document.getElementById(menuId + '-icon');
            if (menu.style.display === "block") {
                menu.style.display = "none";
                icon.innerHTML = "+";
            } else {
                menu.style.display = "block";
                icon.innerHTML = "-";
            }
        }
    </script>

    <div id="menu-container">
        <!-- Power BI Section -->
        <div class="menu-section" onclick="toggleMenu('power-bi')">
            Power BI <span id="power-bi-icon" class="icon">+</span>
        </div>
        <div id="power-bi" class="sub-menu">
            <a href="https://example.com" target="_blank">Dataflow Warehouse</a>
            <a href="https://example.com" target="_blank">Power BI Production</a>
            <a href="https://example.com" target="_blank">Main Power BI App</a>
            <a href="https://example.com" target="_blank">CCMI Uploads</a>
            <a href="https://example.com" target="_blank">All Other Teams Uploads</a>
            <a href="https://example.com" target="_blank">Admin Section</a>
        </div>

        <!-- Power Apps Section -->
        <div class="menu-section" onclick="toggleMenu('power-apps')">
            Power Apps <span id="power-apps-icon" class="icon">+</span>
        </div>
        <div id="power-apps" class="sub-menu">
            <a href="https://example.com" target="_blank">Power BI Admin Centre</a>
            <a href="https://example.com" target="_blank">Power BI Request App</a>
            <a href="https://example.com" target="_blank">MIRA</a>
            <a href="https://example.com" target="_blank">CCMI Workload Tracker</a>
            <a href="https://example.com" target="_blank">CCMI Request App</a>
            <a href="https://example.com" target="_blank">Request App Admin Centre</a>
        </div>

        <!-- SharePoint Section -->
        <div class="menu-section" onclick="toggleMenu('sharepoint')">
            SharePoint <span id="sharepoint-icon" class="icon">+</span>
        </div>
        <div id="sharepoint" class="sub-menu">
            <a href="https://example.com" target="_blank">SharePoint Trackers</a>
            <a href="https://example.com" target="_blank">SharePoint Sites</a>
        </div>

        <!-- SAP Section -->
        <div class="menu-section" onclick="toggleMenu('sap')">
            SAP <span id="sap-icon" class="icon">+</span>
        </div>
        <div id="sap" class="sub-menu">
            <a href="https://example.com" target="_blank">SAP Business Warehouse</a>
            <a href="https://example.com" target="_blank">SAP UI5 (Unplanned Interruptions)</a>
            <a href="https://example.com" target="_blank">401 Unplanned Interruptions Data</a>
            <a href="https://example.com" target="_blank">SAP CRM Password</a>
        </div>

        <!-- Telephony Section -->
        <div class="menu-section" onclick="toggleMenu('telephony')">
            Telephony <span id="telephony-icon" class="icon">+</span>
        </div>
        <div id="telephony" class="sub-menu">
            <a href="https://example.com" target="_blank">eGain</a>
            <a href="https://example.com" target="_blank">Verint</a>
            <a href="https://example.com" target="_blank">AWS</a>
        </div>

        <!-- Citrix Section -->
        <div class="menu-section" onclick="toggleMenu('citrix')">
            Citrix <span id="citrix-icon" class="icon">+</span>
        </div>
        <div id="citrix" class="sub-menu">
            <a href="https://example.com" target="_blank">Arc Catalog</a>
            <a href="https://example.com" target="_blank">Esri Maps</a>
            <a href="https://example.com" target="_blank">Virtual Machines</a>
        </div>

        <!-- Zohodesk Section -->
        <div class="menu-section" onclick="toggleMenu('zohodesk')">
            Zohodesk <span id="zohodesk-icon" class="icon">+</span>
        </div>
        <div id="zohodesk" class="sub-menu">
            <a href="https://example.com" target="_blank">Zohodesk</a>
        </div>
    </div>
    """
    components.html(menu_html, height=290, scrolling=True)
