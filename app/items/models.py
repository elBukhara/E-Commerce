from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base
from typing import Optional

class ItemOrm(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]]
