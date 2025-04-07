import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
import os
import json

class PDFTextExtractor:
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def extract_text(self, pdf_path: str) -> List[str]:
        # Check if the file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File '{pdf_path}' not found!")

        documents = []
        doc = fitz.open(pdf_path)

        for page in doc:
            text = page.get_text("text")
            documents.append(text)

        doc.close()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        )
        chunks = text_splitter.split_text("\n".join(documents))

        print(f"\nChunked text numbers: {len(chunks)}")
        return chunks
if __name__ == "__main__":
    extractor = PDFTextExtractor()
    pdf_path = "data/790-qd-dhcntt_28-9-22_quy_che_dao_tao.pdf"
    documents = extractor.extract_text(pdf_path)

    output_file = "data/chunked_texts.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=4)
