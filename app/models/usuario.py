from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Usuario(Base):
    nome = Column(VARCHAR(50), nullable=False)
    senha = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(50),unique=True, nullable=False)
    celular =Column(VARCHAR(12),unique=True,nullable=False)
    sexo= Column(VARCHAR(11), nullable=False)
    nascimento=Column(Date(), nullable=False)
    cpf=Column(VARCHAR(11), nullable=False)
    estado=Column(VARCHAR(2), nullable=False)
    cidade=Column(VARCHAR(50), nullable=False)
    cep=Column(VARCHAR(20), nullable=False)
    bairro=Column(VARCHAR(100), nullable=False)
    rua=Column(VARCHAR(100), nullable=False)
    numero=Column(VARCHAR(20), nullable=False)
    complemento=Column(VARCHAR(100), nullable=False)
    receber_noticias=Column(Boolean(), nullable=False)
    codigo_troca_senha=Column(VARCHAR(32))
    expiracao=Column(Date())
    saldo=Column(Float())