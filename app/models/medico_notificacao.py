from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Medico_Notificacoes(Base):
    id_medico=Column(ForeignKey('medico.id'),nullable=False)
    id_notificacao=Column(ForeignKey('notificacoes.id'),nullable=False)