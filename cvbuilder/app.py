import streamlit as st # type: ignore
from cv_generator import generate_cv

# Load custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply CSS
load_css()

st.title("📄 Interactive CV Builder")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile (Optional)")
summary = st.text_area("Professional Summary")
education = st.text_area("Education")
experience = st.text_area("Experience")
skills = st.text_area("Skills (comma-separated)")

if st.button("Generate CV"):
    if name and email and phone and summary and education and experience and skills:
        pdf_path = generate_cv(name, email, phone, linkedin, summary, education, experience, skills)
        with open(pdf_path, "rb") as pdf_file:
            st.download_button("📥 Download CV", pdf_file, file_name="generated_cv.pdf", key="download_cv")
    else:
        st.error("⚠️ Please fill in all required fields.")
