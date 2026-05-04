import pdfplumber
from docx import Document


def extract_pdf_text(file):
    text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_docx_text(file):
    text = ""

    doc = Document(file.file)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_resume_txt(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file)

    elif filename.endswith(".docx"):
        return extract_docx_text(file)

    else:
        raise ValueError(
            "Unsupported file format. Upload PDF or DOCX only."
        )