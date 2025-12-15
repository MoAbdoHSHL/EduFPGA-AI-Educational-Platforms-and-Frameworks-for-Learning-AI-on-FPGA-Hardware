import streamlit as st

# Hide everything, show only website
st.set_page_config(layout="wide")

# Remove all Streamlit styling
st.markdown("""
<style>
    /* Remove black frames */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    .stApp {
        padding: 0 !important;
    }
    
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Make iframe full width */
    iframe {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Load and show your website
try:
    with open("framwork.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # Fix image paths
    html = html.replace("getImagePath('", "'")
    html = html.replace("getFullImagePath('", "'")
    html = html.replace("')", "")
    
    # Display full screen
    st.components.v1.html(html, height=1500, scrolling=True)
    
except:
    st.error("framwork.html not found")
