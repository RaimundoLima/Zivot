from .base import Base
from sqlalchemy import Boolean,Date,DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Horarios(Base):
    id_agenda=Column(ForeignKey('agenda.id'),nullable=False)
    horario_inicio=Column(Time(),nullable=False)
    horario_fim=Column(Time(),nullable=False)
    