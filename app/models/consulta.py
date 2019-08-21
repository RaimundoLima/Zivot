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
    online=Column(VARCHAR(50),nullable=False)
    nota_usuario=Column(Float(),nullable=True)
    comentario_usuario=Column(VARCHAR(500),nullable=True)
    nota_medico=Column(Float(),nullable=True)
    comentario_medico=Column(VARCHAR(500),nullable=True)
    codigo_pagseguro=Column(VARCHAR(100),nullable=True)
