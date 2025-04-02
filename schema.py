from typing import List, Optional
from pydantic import BaseModel, Field


# Define schema for the lowest-level entity (Point/Item).
class Point(BaseModel):
    point_number: str = Field(..., description="The number or identifier of the point.")
    content: str = Field(..., description="The content or description of the point.")
    references: Optional[List[str]] = Field(None, description="Any references related to this point.")
    legal_implication: Optional[str] = Field(None, description="The legal implication or effect of this point.")


# Define schema for a Clause/Paragraph.
class Clause(BaseModel):
    clause_number: str = Field(..., description="The number or identifier of the clause.")
    title: Optional[str] = Field(None, description="The title of the clause (if any).")
    content: str = Field(..., description="The content of the clause.")
    references: Optional[List[str]] = Field(None, description="Any references related to this clause.")
    legal_implication: Optional[str] = Field(None, description="The legal implication or effect of this clause.")
    points: Optional[List[Point]] = Field(None, description="The list of points or items in this clause.")


# Define schema for an Article.
class Article(BaseModel):
    article_number: str = Field(..., description="The number or identifier of the article.")
    title: Optional[str] = Field(None, description="The title of the article (if any).")
    content: str = Field(..., description="The content of the article.")
    references: Optional[List[str]] = Field(None, description="Any references related to this article.")
    clauses: List[Clause] = Field(..., description="The list of clauses in this article.")
    legal_implication: Optional[str] = Field(None, description="The legal implication or effect of this article.")


# Define schema for a Section.
class Section(BaseModel):
    section_number: str = Field(..., description="The number or identifier of the section.")
    title: Optional[str] = Field(None, description="The title of the section (if any).")
    content: str = Field(..., description="The content of the section.")
    references: Optional[List[str]] = Field(None, description="Any references related to this section.")
    articles: List[Article] = Field(..., description="The list of articles in this section.")


# Define schema for a Chapter.
class Chapter(BaseModel):
    chapter_number: str = Field(..., description="The number or identifier of the chapter.")
    title: Optional[str] = Field(None, description="The title of the chapter (if any).")
    content: str = Field(..., description="The content of the chapter.")
    references: Optional[List[str]] = Field(None, description="Any references related to this chapter.")
    sections: List[Section] = Field(..., description="The list of sections in this chapter.")


# Define the main schema for the Legal Document.
class LegalDocument(BaseModel):
    title: str = Field(..., description="The title of the legal document (e.g., the name of the law or regulation).")
    date_of_enactment: Optional[str] = Field(None, description="The date the document was enacted.")
    promulgating_authority: Optional[str] = Field(None,
                                                  description="The authority or body that promulgated the document.")
    chapters: List[Chapter] = Field(..., description="The chapters in the legal document.")
    references: Optional[List[str]] = Field(None, description="Any references related to the entire legal document.")
    legal_implications: Optional[str] = Field(None, description="General legal implications of the document.")

