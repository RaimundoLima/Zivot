from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Horarios_extras(Base):
    id_agenda=Column(ForeignKey('agenda.id'),nullable=False)
    horario_inicio=Column(DateTime(),nullable=False)
    horario_fim=Column(DateTime(),nullable=False)
    tipo=Column(VARCHAR(10),nullable=False)
    