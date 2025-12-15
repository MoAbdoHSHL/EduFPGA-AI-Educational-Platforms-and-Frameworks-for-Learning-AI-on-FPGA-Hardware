import streamlit as st
import os

# HIDE SIDEBAR COMPLETELY
st.set_page_config(
    page_title="FPGA AI Boards Guide",
    layout="wide",
    initial_sidebar_state="collapsed"  # This hides the sidebar
)

# Add custom CSS to hide sidebar permanently
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Make the main area full width */
    .main .block-container {
        padding-top: 0;
        padding-right: 0;
        padding-left: 0;
        padding-bottom: 0;
        max-width: 100%;
    }
    
    /* Hide the sidebar hamburger menu */
    [data-testid="collapsedControl"] {
        display: none;
    }
    
    /* Remove extra padding */
    .stApp {
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)

# Load and display your HTML website FULL SCREEN
try:
    with open("framwork.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Display website full screen
    st.components.v1.html(html_content, height=2000, scrolling=True)
    
except FileNotFoundError:
    # Fallback if framwork.html not found
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    if html_files:
        with open(html_files[0], "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    else:
        st.error("HTML file not found")