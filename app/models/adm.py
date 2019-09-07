from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Adm(Base):
    senha = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(50),unique=True, nullable=False)
