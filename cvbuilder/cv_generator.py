from fpdf import FPDF  # type: ignore
import re

def clean_text(text):
    """Removes unsupported characters from text."""
    if text:
        return re.sub(r'[^\x20-\x7E]+', '', text)  # Keep only standard ASCII characters
    return ""

def generate_cv(name, email, phone, linkedin, summary, education, experience, skills):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Check if Arial is available, fallback to Helvetica
    font_name = "Arial"
    try:
        pdf.set_font(font_name, 'B', 24)
    except:
        font_name = "Helvetica"
        pdf.set_font(font_name, 'B', 24)

    # Header - Set name to BLACK color
    pdf.set_text_color(0, 0, 0)  # Changed from blue to black
    pdf.cell(200, 15, clean_text(name), ln=True, align='C')
    
    # Contact Details
    pdf.set_font(font_name, 'I', 12)
    pdf.cell(200, 10, clean_text(f"{email} | {phone}"), ln=True, align='C')
    if linkedin:
        pdf.cell(200, 10, clean_text(linkedin), ln=True, align='C')
    pdf.ln(10)

    # Section Details
    sections = {
        "Professional Summary": summary,
        "Education": education,
        "Experience": experience,
        "Skills": skills.replace(',', '\n')
    }

    for title, content in sections.items():
        pdf.set_font(font_name, 'B', 18)
        pdf.set_text_color(255, 69, 0)  # Orange color for section titles
        pdf.cell(0, 10, clean_text(title), ln=True)
        
        pdf.set_font(font_name, size=12)
        pdf.set_text_color(0, 0, 0)  # Black color for section content
        pdf.multi_cell(0, 8, clean_text(content))
        pdf.ln(5)

    # Footer
    pdf.set_y(-20)
    pdf.set_font(font_name, 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Generated with Interactive CV Builder", align='C')

    file_path = "generated_cv.pdf"
    pdf.output(file_path, "F")
    return file_path
