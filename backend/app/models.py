from sqlalchemy import Column, Integer, String
from .database import Base  


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    grade_class = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    expectations = Column(String)
    hashed_password = Column(String, nullable=False)
