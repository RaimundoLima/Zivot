from .base import Base
from sqlalchemy import DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Notificacoes(Base):
    titulo = Column(VARCHAR(50), nullable=False)
    descricao= Column(VARCHAR(200),nullable=False)
    #usuario_notificacoes=relationship('usuario_notificacoes',backref='notificacao',lazy=True)
    #medico_notificacoes=relationship('medico_notificacoes',backref='notificacao',lazy=True)
