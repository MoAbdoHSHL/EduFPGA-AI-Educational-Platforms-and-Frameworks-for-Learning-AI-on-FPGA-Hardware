import streamlit as st
import os
import base64

# COMPLETELY HIDE EVERYTHING EXCEPT YOUR WEBSITE
st.set_page_config(
    page_title="FPGA AI Boards Guide",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# RADICAL CSS TO REMOVE ALL STREAMLIT STYLING
st.markdown("""
<style>
    /* Hide everything Streamlit */
    .stApp > header {
        display: none;
    }
    
    [data-testid="stSidebar"] {
        display: none;
    }
    
    [data-testid="collapsedControl"] {
        display: none;
    }
    
    /* Remove ALL padding and margins */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Make iframe full screen */
    iframe {
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        display: block !important;
    }
    
    /* Hide any remaining Streamlit elements */
    .st-emotion-cache-1y4p8pa {
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Function to embed images as base64
def embed_images_as_base64(html_content):
    """Convert local image references to base64 data URIs"""
    import re
    import base64
    
    # Pattern to find image references
    pattern = r'src=["\']([^"\']+\.(jpg|jpeg|png|gif))["\']'
    
    def replace_with_base64(match):
        img_path = match.group(1)
        try:
            # Check if file exists
            if os.path.exists(img_path):
                with open(img_path, "rb") as img_file:
                    encoded = base64.b64encode(img_file.read()).decode()
                extension = img_path.split('.')[-1].lower()
                mime_type = f"image/{'jpeg' if extension == 'jpg' else extension}"
                return f'src="data:{mime_type};base64,{encoded}"'
            else:
                # Try to find the image in current directory
                for file in os.listdir('.'):
                    if file.lower() == img_path.lower():
                        with open(file, "rb") as img_file:
                            encoded = base64.b64encode(img_file.read()).decode()
                        extension = file.split('.')[-1].lower()
                        mime_type = f"image/{'jpeg' if extension == 'jpg' else extension}"
                        return f'src="data:{mime_type};base64,{encoded}"'
                print(f"⚠️ Image not found: {img_path}")
                return match.group(0)
        except Exception as e:
            print(f"⚠️ Error embedding {img_path}: {e}")
            return match.group(0)
    
    return re.sub(pattern, replace_with_base64, html_content, flags=re.IGNORECASE)

try:
    # Read your HTML
    with open("framwork.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # FIX 1: Embed images as base64
    html_content = embed_images_as_base64(html_content)
    
    # FIX 2: Remove JavaScript image loading functions that might fail
    html_content = html_content.replace("getImagePath('", "'")
    html_content = html_content.replace("getFullImagePath('", "'")
    html_content = html_content.replace("handleImageError", "// handleImageError")
    
    # FIX 3: Add responsive CSS to HTML
    responsive_css = """
    <style>
        body { 
            margin: 0 !important; 
            padding: 0 !important;
            width: 100vw !important;
            overflow-x: hidden !important;
        }
        .container, .main-content {
            width: 100% !important;
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
    """
    
    # Insert CSS at the beginning
    if '</head>' in html_content:
        html_content = html_content.replace('</head>', f'{responsive_css}</head>')
    else:
        html_content = responsive_css + html_content
    
    # Display FULL SCREEN
    st.components.v1.html(html_content, height=2000, scrolling=True, width=None)
    
except FileNotFoundError:
    st.error("❌ framwork.html not found")
    st.code("Files in directory: " + ", ".join(os.listdir('.')))