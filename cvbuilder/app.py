import streamlit as st
import os

# Function to load CSS
def load_css():
    css_file = "style.css"  # Ensure this file exists in the same directory
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Style file (style.css) not found. Default styling applied.")

# Load CSS at startup
load_css()

# App UI
st.title("Interactive CV Builder")
st.write("Generate a professional CV with ease.")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile URL")
summary = st.text_area("Professional Summary")
education = st.text_area("Education")
experience = st.text_area("Experience")
skills = st.text_area("Skills (comma-separated)")

if st.button("Generate CV"):
    from cv_generator import generate_cv
    file_path = generate_cv(name, email, phone, linkedin, summary, education, experience, skills)
    
    with open(file_path, "rb") as f:
        st.download_button("📥 Download CV", f, file_name="Generated_CV.pdf", mime="application/pdf")
