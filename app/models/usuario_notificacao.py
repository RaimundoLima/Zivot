from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Usuario_Notificacoes(Base):
    id_usuario=Column(ForeignKey('usuario.id'),nullable=False)
    id_notificacao=Column(ForeignKey('notificacoes.id'),nullable=False)