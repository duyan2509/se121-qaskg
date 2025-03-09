import os
from docx import Document

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')
OUTPUT_DIR = os.path.join(DATA_DIR, 'processed')  # Thư mục chứa file kết quả (.txt)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def convert_docx_to_txt(docx_file, txt_file):
    doc = Document(docx_file)
    content = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            content.append(paragraph.text.strip())

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))

    print(f"Đã chuyển đổi {docx_file} sang {txt_file}.")


for filename in os.listdir(RAW_DIR):
    if filename.endswith('.docx'):
        docx_file = os.path.join(RAW_DIR, filename)
        txt_file = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.txt")

        convert_docx_to_txt(docx_file, txt_file)
