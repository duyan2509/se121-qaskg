from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from typing import List
import os


class PDFTextExtractor:
    def __init__(self, pdf_data_path: str = "data", chunk_size: int = 512, chunk_overlap: int = 50):
        self.pdf_data_path = pdf_data_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def extract_text(self) -> List[str]:
        if not os.path.exists(self.pdf_data_path):
            raise FileNotFoundError(f"Folder '{self.pdf_data_path}' not found!")

        print(f"\n📂 Checking path: {self.pdf_data_path}")
        # Khởi tạo loader để quét tất cả các file PDF trong thư mục "data"
        loader = DirectoryLoader(self.pdf_data_path, glob="*.pdf", loader_cls=PyPDFLoader)

        print("\n📄 Loading PDF files...")
        documents = loader.load()

        # Chia nhỏ văn bản thành từng đoạn nhỏ
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        )
        chunks = text_splitter.split_documents(documents)

        # Danh sách chứa toàn bộ văn bản đã chia nhỏ
        document_texts = [chunk.page_content for chunk in chunks]

        print(f"\n✅ Tổng số đoạn văn bản trích xuất: {len(document_texts)}")
        return document_texts


if __name__ == "__main__":
    extractor = PDFTextExtractor()
    documents = extractor.extract_text()

    print("\n Một số đoạn văn bản đầu tiên:")
    for i, doc in enumerate(documents[:5]):
        print(f"\n🔹 Đoạn {i + 1}: {doc[:200]}...")