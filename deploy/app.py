import streamlit as st

# COMPLETELY remove black frames
st.set_page_config(
    page_title="FPGA AI Guide",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove ALL Streamlit styling
st.markdown("""
<style>
    /* REMOVE BLACK FRAMES */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        padding: 0rem !important;
        margin: 0 !important;
    }
    
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Hide hamburger menu */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Fix iframe */
    iframe {
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Load and display your website
try:
    with open("framwork.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # Fix image paths for Streamlit
    html = html.replace("getImagePath('", "'")
    html = html.replace("getFullImagePath('", "'")
    html = html.replace("')", "")
    html = html.replace('")', '"')
    
    # Display full screen
    st.components.v1.html(html, height=2000, scrolling=True)
    
except Exception as e:
    st.error(f"Error loading website: {e}")
