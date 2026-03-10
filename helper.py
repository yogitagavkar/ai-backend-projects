import pdfplumber

def extract_resume_txt(file):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text +=page.extract_text()
        
    return text