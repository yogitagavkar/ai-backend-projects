import pdfplumber
from docx import Document
from io import BytesIO


async def extract_pdf_text(file):
    text = ""

    content = await file.read()

    pdf_file = BytesIO(content)

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


async def extract_docx_text(file):
    text = ""

    content = await file.read()

    doc_file = BytesIO(content)

    doc = Document(doc_file)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


async def extract_resume_txt(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return await extract_pdf_text(file)

    elif filename.endswith(".docx"):
        return await extract_docx_text(file)

    else:
        raise ValueError(
            "Unsupported file format. Upload PDF or DOCX only."
        )