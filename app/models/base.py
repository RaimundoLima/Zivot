from app import db
import json

class Base(db.Model):
    __abstract__=True

    id=db.Column(db.Integer(),primary_key=True)
    date_criacao=db.Column(db.DateTime(),default=db.func.current_timestamp())

    def inserir(self):
        db.session.add(self)
        db.session.commit()
        return True

    def buscar(self):
        return  self.query.filter_by(id=self.id).first()

    def buscarId(self,id):
        return  self.query.filter_by(id=id).first()

    def deletar(self):
        db.session.deletar(self)
        db.session.commit()
        return True

    def listar(self):
        return self.query.all()

    def buscaGenerica(self,kBusca):
        return self.query.filter_by(**kBusca).first()

    def buscaGenericaLista(self,kBusca):
        return self.query.filter_by(**kBusca)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def toJson(self):
        return json.dumps(self.as_dict(),default=str)
    
