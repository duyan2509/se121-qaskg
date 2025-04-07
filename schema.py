from typing import List, Optional, Dict, Union
from datetime import date
from pydantic import BaseModel, Field


class Point(BaseModel):
    """Mô hình cho một điểm trong văn bản pháp lý."""
    point_number: str = Field(..., description="Số hiệu của điểm")
    point_content: str = Field(..., description="Nội dung của điểm")


class Clause(BaseModel):
    """Mô hình cho một khoản trong văn bản pháp lý."""
    clause_number: str = Field(..., description="Số hiệu của khoản")
    clause_content: str = Field(..., description="Nội dung của khoản")
    has_direct_content: bool = Field(False, description="Khoản có nội dung trực tiếp không")
    points: Optional[List[Point]] = Field(None, description="Danh sách các điểm trong khoản")


class Article(BaseModel):
    """Mô hình cho một điều trong văn bản pháp lý."""
    article_number: str = Field(..., description="Số hiệu của điều")
    article_title: Optional[str] = Field(None, description="Tiêu đề của điều")
    article_content: Optional[str] = Field(None, description="Nội dung của điều")
    has_direct_content: bool = Field(False, description="Điều có nội dung trực tiếp không")
    clauses: Optional[List[Clause]] = Field(None, description="Danh sách các khoản trong điều")


class Section(BaseModel):
    """Mô hình cho một mục trong văn bản pháp lý."""
    section_number: str = Field(..., description="Số hiệu của mục")
    section_title: str = Field(..., description="Tiêu đề của mục")
    section_content: Optional[str] = Field(None, description="Nội dung của mục")
    articles: List[Article] = Field(default_factory=list, description="Danh sách các điều trong mục")


class Chapter(BaseModel):
    """Mô hình cho một chương trong văn bản pháp lý."""
    chapter_number: str = Field(..., description="Số hiệu của chương")
    chapter_title: str = Field(..., description="Tiêu đề của chương")
    chapter_content: Optional[str] = Field(None, description="Nội dung của chương")
    sections: Optional[List[Section]] = Field(None, description="Danh sách các mục trong chương")
    articles: Optional[List[Article]] = Field(None, description="Danh sách các điều trực tiếp trong chương")


class Signer(BaseModel):
    """Mô hình cho người ký văn bản pháp lý."""
    name: str = Field(..., description="Tên người ký")
    position: str = Field(..., description="Chức vụ người ký")


class Party(BaseModel):
    """Mô hình cho một bên liên quan trong văn bản pháp lý."""
    party_name: str = Field(..., description="Tên của bên")
    party_type: str = Field(..., description="Loại bên (tổ chức hoặc cá nhân)")
    address: Optional[str] = Field(None, description="Địa chỉ của bên")
    representative: Optional[str] = Field(None, description="Người đại diện")
    position: Optional[str] = Field(None, description="Chức vụ")
    contact_info: Optional[str] = Field(None, description="Thông tin liên hệ")


class LegalReference(BaseModel):
    """Mô hình cho tham chiếu pháp lý."""
    referenced_document: str = Field(..., description="Văn bản được tham chiếu")
    referenced_article: Optional[str] = Field(None, description="Điều khoản được tham chiếu")
    content: Optional[str] = Field(None, description="Nội dung tham chiếu")


class FinancialTerms(BaseModel):
    """Mô hình cho điều khoản tài chính."""
    currency: str = Field(..., description="Loại tiền tệ")
    amounts: List[float] = Field(default_factory=list, description="Các số tiền")
    payment_terms: Optional[str] = Field(None, description="Điều khoản thanh toán")


class Deadline(BaseModel):
    """Mô hình cho thời hạn trong văn bản pháp lý."""
    description: str = Field(..., description="Mô tả về thời hạn")
    date: date = Field(..., description="Ngày thời hạn")
    related_article: Optional[str] = Field(None, description="Điều khoản liên quan")


class LegalDocument(BaseModel):
    """Mô hình cho văn bản pháp lý."""
    document_number: str = Field(..., description="Số hiệu văn bản")
    document_title: str = Field(..., description="Tiêu đề văn bản")
    document_type: str = Field(..., description="Loại văn bản")
    issuing_authority: str = Field(..., description="Cơ quan ban hành")
    issue_date: date = Field(..., description="Ngày ban hành")
    effective_date: Optional[date] = Field(None, description="Ngày hiệu lực")

    signer: Signer = Field(..., description="Người ký văn bản")
    chapters: Optional[List[Chapter]] = Field(None, description="Danh sách các chương")
    articles: Optional[List[Article]] = Field(None, description="Danh sách các điều trực tiếp")
    parties: Optional[List[Party]] = Field(None, description="Danh sách các bên liên quan")
    legal_references: Optional[List[LegalReference]] = Field(None, description="Danh sách tham chiếu pháp lý")
    financial_terms: Optional[FinancialTerms] = Field(None, description="Điều khoản tài chính")
    deadlines: Optional[List[Deadline]] = Field(None, description="Danh sách các thời hạn")

