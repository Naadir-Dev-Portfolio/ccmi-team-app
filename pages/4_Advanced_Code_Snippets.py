import streamlit as st
from menu import render_menu
from style import inject_css


st.set_page_config(page_title="Advanced Code Snippets", layout="wide")
inject_css()

# Sidebar content (same across all pages)
with st.sidebar:
    st.markdown("### Shortcut Links")
    render_menu()
    st.image("static/teamlogo2.png", use_column_width=True)
    st.markdown("<div class='sidebar-footer'>Made for the CCMI Team</div>", unsafe_allow_html=True)

# Main content for Advanced Code Snippets
st.title("Advanced Code Snippets")

snippet_options = ["Power Query", "Excel Formulas", "VBA Code"]
selected_snippet = st.selectbox("Select Code Type:", snippet_options)

if selected_snippet == "Power Query":
    st.code("""
    let
        Source = Excel.Workbook(File.Contents("C:\\path\\to\\your\\file.xlsx"), null, true),
        Sheet1 = Source{[Name="Sheet1"]}[Data],
        #"Changed Type" = Table.TransformColumnTypes(Sheet1,{{"Column1", type text}, {"Column2", type number}})
    in
        #"Changed Type"
    """, language="powerquery")
elif selected_snippet == "Excel Formulas":
    st.code("""
    =IF(A1>10, "Greater than 10", "Less than or equal to 10")
    """, language="excel")
elif selected_snippet == "VBA Code":
    st.code("""
    Sub HelloWorld()
        MsgBox "Hello, World!"
    End Sub
    """, language="vba")
