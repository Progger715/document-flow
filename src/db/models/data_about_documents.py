"""data_about_documents model file"""

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column
from .base import Base


class DataAboutDocuments(Base):
    __tablename__ = "data_about_documents"

    inner_number = mapped_column(String(100), nullable=False)
    output_number = mapped_column(String(100), nullable=False)
    output_date = mapped_column(DateTime, nullable=False)
    type_document = mapped_column(String(100), nullable=False)
    name = mapped_column(String(100), nullable=False)
    date_creating = mapped_column(DateTime, nullable=False)
    id_creator = mapped_column(Integer, ForeignKey("users.id", ondelete='SET NULL'))
