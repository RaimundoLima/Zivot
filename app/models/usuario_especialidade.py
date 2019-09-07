from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Usuario_Especialidade(Base):
    id_usuario=Column(ForeignKey('usuario.id'),nullable=False)
    id_especialidade=Column(ForeignKey('especialidade.id'),nullable=False)