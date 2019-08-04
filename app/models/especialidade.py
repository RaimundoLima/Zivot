from .base import Base
from sqlalchemy import DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Especialidade(Base):
    nome = Column(VARCHAR(100), nullable=False)
    medicos=relationship('Medico',backref='especialidade',lazy=True)
    #usuario_especialidade=relationship('usuario_especialidade',backref='especialidade',lazy=True)
