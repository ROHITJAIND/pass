import streamlit as st
import os

def load_css(file_name):
    """Loads CSS content from a file."""
    try:
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: CSS file '{file_name}' not found.")

def load_html(file_name):
    """Loads HTML content from a file."""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: HTML file '{file_name}' not found."

# Load CSS files
load_css("bootstrap.min.css")
load_css("font-awesome.css")
load_css("style.css")

# Display the HTML content
html_content = load_html("transport.html")
st.components.v1.html(html_content, height=800, scrolling=True)

# You can add other Streamlit components here if needed
st.write("---")
st.write("This is a Streamlit app displaying the content of transport.html.")

# To handle images, you would need to serve them or embed them differently.
# For now, the paths in transport.html (like ./logo.png) will not work directly
# unless Streamlit is configured to serve static files from that location.
# For simple cases, consider base64 encoding small images directly into the HTML/CSS
# or uploading them to a public accessible URL and updating the paths in transport.html.

# Example of embedding an image (you would need to read the image file first)
# For 'rohit jain.JPG' and 'QR.png', you would need to adjust the HTML
# or serve them as static files with Streamlit.
# st.image("rohit jain.JPG")
# st.image("QR.png")