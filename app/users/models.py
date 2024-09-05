from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from database import Base

class UserOrm(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))  # Store hashed password
    
    carts = relationship("CartOrm", back_populates="user")