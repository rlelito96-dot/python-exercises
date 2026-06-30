# Imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    website = Column(String)
    age = Column(Integer)
    role = Column(String)
    password_hash = Column(String, nullable=False)
