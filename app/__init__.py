from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("configs.cfg")

from app.blueprints import index, errors, teste

app.register_blueprint(index)
app.register_blueprint(errors)
app.register_blueprint(teste)

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
db.init_app(app)
from app.models import Usuario

from app.utils.flask_mail import mail
mail.init_app(app)


with app.app_context():
    db.create_all()





