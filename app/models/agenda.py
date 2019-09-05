from .base import Base
from sqlalchemy import DateTime,Time,ForeignKey,Column, Integer, Numeric, Binary, String,VARCHAR,Float
from sqlalchemy.orm import relationship

class Agenda(Base):
    id_medico=Column(ForeignKey("medico.id"))
    dia_semana=Column(VARCHAR(20))