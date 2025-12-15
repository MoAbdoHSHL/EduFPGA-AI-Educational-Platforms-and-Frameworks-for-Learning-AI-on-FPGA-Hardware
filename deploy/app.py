import streamlit as st
import os

st.set_page_config(
    page_title="FPGA AI Guide",
    layout="wide"
)

try:
    with open("framwork.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
except:
    st.error("HTML file not found")

with st.sidebar:
    st.title("Controls")
    search = st.text_input("Search")
    vendor = st.selectbox("Vendor", ["All", "Xilinx", "Intel", "Lattice"])
    if st.button("Apply"):
        st.success("Filters applied")
