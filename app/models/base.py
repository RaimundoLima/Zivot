from app import db

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

    def deletar(self):
        db.session.deletar(self)
        db.session.commit()
        return True

    def listar(self):
        return self.query.all()