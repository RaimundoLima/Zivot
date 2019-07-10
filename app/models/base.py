from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Base(db.Model):
    __abstract__=True

    id=db.Column(db.Integer,primary_key=True)
    date_created=db.Column(db.DateTime,default=db.func.current_timestamp())
    date_modified=db.Column(db.DateTime,default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

    def inserir(self):
        db.session.add(self)
        db.session.commit(self)
        return True

    def buscar(self):
        return  self.query.filter_by(id=self.id).first()

    def deletar(self):
        db.ssession.deletar(self)
        db.session.commit()
        return True

    def listar(self):
        return self.query.all()