from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class CoCriador(Base):
    id_medico=Column(ForeignKey('medico.id'))
    medico=relationship('medico',backref='coCriador',lazy=True)
