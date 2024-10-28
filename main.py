import streamlit as st

# Title for the app
st.title("BOQ Generator")

# File uploader
uploaded_file = st.file_uploader("Upload your Architectural Drawing or Specification File", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    st.write("File uploaded successfully!")

