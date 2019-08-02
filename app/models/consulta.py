from .base import Base
from sqlalchemy import DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Consulta(Base):
    id_usuario=Column(ForeignKey('usuario.id'),nullable=False)
    id_medico=Column(ForeignKey('medico.id'),nullable=False)
    horario_inicio=Column(DateTime(),nullable=False)
    horario_fim=Column(DateTime(),nullable=False)
    valor=Column(Float(),nullable=False)
    status=Column(VARCHAR(50),nullable=False)
    nota_usuario=Column(Float(),nullable=False)
    comentario_usuario=Column(VARCHAR(500),nullable=False)
    nota_medico=Column(Float(),nullable=False)
    comentario_medico=Column(VARCHAR(500),nullable=False)
    codigo_pagseguro=Column(VARCHAR(100),nullable=False)
