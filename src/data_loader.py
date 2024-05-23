# src/data_loader.py
import fitz  # PyMuPDF

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def save_to_txt(text, output_path):
    with open(output_path, 'w') as file:
        file.write(text)

if __name__ == "__main__":
    pdf_path = "../data/milestone_policies.pdf"
    text_output_path = "../data/milestone_policies.txt"
    pdf_text = load_pdf(pdf_path)
    save_to_txt(pdf_text, text_output_path)
