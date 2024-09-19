import streamlit.components.v1 as components

# First Menu (CCMI Team, Power BI, SharePoint, etc.)
# First Menu (CCMI Team, Power BI, SharePoint, etc.)
def render_menu_1():
    menu_html = """
    <style>
        body, .menu-section, .sub-menu a {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .menu-section {
            cursor: pointer;
            font-size: 14px;
            margin: 2px 0;
            padding: 8px;
            background-color: #2c2c2e;
            color: #ffffff;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.3s ease;
        }

        .menu-section:hover {
            background-color: #3a3a3d;
        }

        .sub-menu {
            display: none;
            margin-left: 15px;
            font-size: 13px;
            color: #b3b3b3;
        }

        .sub-menu a {
            display: block;
            padding: 6px 10px;
            color: #ffffff;
            background-color: #2e2e2f;
            margin: 2px 0;
            text-decoration: none; /* No underline on sub-menu links */
            border-radius: 5px;
            transition: background-color 0.2s;
        }

        .sub-menu a:hover {
            background-color: #3a3a3d;
            color: #ffffff;
        }

        /* Remove underline from main menu links (like Citrix and ZohoDesk) */
        a {
            text-decoration: none;
            color: inherit; /* Inherit color from the parent */
        }

        a:hover {
            text-decoration: none; /* No underline on hover */
        }

        .icon {
            font-size: 16px;
            color: #ffffff;
        }

        /* Custom scroll bar styling for sub-menus */
        .sub-menu {
            max-height: 150px;
            overflow-y: auto;
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
    </style>

    <script>
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
        <!-- CCMI Team Section -->
        <div class="menu-section" onclick="toggleMenu('ccmi-team')">
            CCMI Team <span id="ccmi-team-icon" class="icon">+</span>
        </div>
        <div id="ccmi-team" class="sub-menu">
            <a href="https://example.com" target="_blank">Sharepoint Site</a>
            <a href="https://example.com" target="_blank">Team Drive</a>
            <a href="https://example.com" target="_blank">121 Packs</a>
            <a href="https://example.com" target="_blank">Videos</a>
            <a href="https://example.com" target="_blank">Team Projects</a>
            <a href="https://example.com" target="_blank">Webmail</a>
            <a href="https://example.com" target="_blank">Open Requests</a>
            <a href="https://example.com" target="_blank">Team Planner</a>
        </div>

        <!-- Power BI Section -->
        <div class="menu-section" onclick="toggleMenu('power-bi')">
            Power BI <span id="power-bi-icon" class="icon">+</span>
        </div>
        <div id="power-bi" class="sub-menu">
            <a href="https://example.com" target="_blank">Power BI</a>
            <a href="https://example.com" target="_blank">Dataflow Warehouse</a>
            <a href="https://example.com" target="_blank">Report Production Warehouse</a>
            <a href="https://example.com" target="_blank">Power BI Bridge</a>
            <a href="https://example.com" target="_blank">eGain Health Check</a>
            <a href="https://example.com" target="_blank">Sharepoint Site</a>
            <a href="https://example.com" target="_blank">CCMI Upload Area</a>
            <a href="https://example.com" target="_blank">Business Upload Area</a>
            <a href="https://example.com" target="_blank">PBIX Files</a>
        </div>

        <!-- SharePoint Section -->
        <div class="menu-section" onclick="toggleMenu('sharepoint')">
            SharePoint <span id="sharepoint-icon" class="icon">+</span>
        </div>
        <div id="sharepoint" class="sub-menu">
            <a href="https://example.com" target="_blank">Groups</a>
            <a href="https://example.com" target="_blank">CCMI SharePoint Lists</a>
            <a href="https://example.com" target="_blank">All SharePoint Lists</a>
            <a href="https://example.com" target="_blank">Request Logs</a>
            <a href="https://example.com" target="_blank">Group Audit List</a>
            <a href="https://example.com" target="_blank">GSOP Payment Errors</a>
        </div>

        <!-- Shared Drive Section -->
        <div class="menu-section" onclick="toggleMenu('sharedrive')">
            Shared Drive <span id="sharedrive-icon" class="icon">+</span>
        </div>
        <div id="sharedrive" class="sub-menu">
            <a href="https://example.com" target="_blank">All Shared Drive Areas</a>
            <a href="https://example.com" target="_blank">Handover Documents</a>
        </div>

        <!-- SAP Section -->
        <div class="menu-section" onclick="toggleMenu('sap')">
            SAP <span id="sap-icon" class="icon">+</span>
        </div>
        <div id="sap" class="sub-menu">
            <a href="https://example.com" target="_blank">Business Warehouse</a>
            <a href="https://example.com" target="_blank">UI5 Validation</a>
            <a href="https://example.com" target="_blank">Unplanned Finalized Data (401)</a>
            <a href="https://example.com" target="_blank">CRM Password Vault</a>
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

        <!-- Citrix (No submenu, direct link) -->
        <div class="menu-section">
            <a href="https://example.com" target="_blank" style="color: #ffffff;">Citrix</a>
        </div>

        <!-- ZohoDesk (No submenu, direct link) -->
        <div class="menu-section">
            <a href="https://example.com" target="_blank" style="color: #ffffff;">ZohoDesk</a>
        </div>

        <!-- Other Systems Section -->
        <div class="menu-section" onclick="toggleMenu('other-systems')">
            Other Systems <span id="other-systems-icon" class="icon">+</span>
        </div>
        <div id="other-systems" class="sub-menu">
            <a href="https://example.com" target="_blank">ServiceNow</a>
            <a href="https://example.com" target="_blank">Rand and Rave</a>
            <a href="https://example.com" target="_blank">AQAD</a>
            <a href="https://example.com" target="_blank">Gov Streetworks</a>
        </div>
    </div>
    """
    components.html(menu_html, height=400, scrolling=True)


def render_menu_2():
    menu_html = """
    <style>
        body, .menu-section, .sub-menu a {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .menu-section {
            cursor: pointer;
            font-size: 14px;
            margin: 2px 0;
            padding: 8px;
            background-color: #2c2c2e;
            color: #ffffff;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.3s ease;
        }

        .menu-section:hover {
            background-color: #3a3a3d;
        }

        .sub-menu {
            display: none;
            margin-left: 15px;
            font-size: 13px;
            color: #b3b3b3;
        }

        .sub-menu a {
            display: block;
            padding: 6px 10px;
            color: #ffffff;
            background-color: #2e2e2f;
            margin: 2px 0;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.2s;
        }

        .sub-menu a:hover {
            background-color: #3a3a3d;
            color: #ffffff;
        }

        /* Remove underline from main menu links */
        a {
            text-decoration: none;
            color: inherit;
        }

        a:hover {
            text-decoration: none;
        }

        .icon {
            font-size: 16px;
            color: #ffffff;
        }

        /* Custom scroll bar styling for sub-menus */
        .sub-menu {
            max-height: 150px;
            overflow-y: auto;
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
    </style>

    <script>
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
        <!-- Power Apps (Direct link) -->
        <div class="menu-section">
            <a href="https://example.com" target="_blank" style="color: #ffffff;">Power Apps</a>
        </div>

        <!-- Power Automate Section with Submenu -->
        <div class="menu-section" onclick="toggleMenu('power-automate')">
            Power Automate <span id="power-automate-icon" class="icon">+</span>
        </div>
        <div id="power-automate" class="sub-menu">
            <a href="https://example.com" target="_blank">CSAT Daily Flow</a>
            <a href="https://example.com" target="_blank">RIIO Score Card Flow</a>
            <a href="https://example.com" target="_blank">Enquiries Score Card Flow</a>
            <a href="https://example.com" target="_blank">Weekly Call Performance Flow</a>
        </div>
    </div>
    """
    components.html(menu_html, height=150, scrolling=True)
