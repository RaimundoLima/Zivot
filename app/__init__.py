from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("configs.cfg")

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
db.init_app(app)
from app.models import Usuario

from app.blueprints import nologin, errors, teste

app.register_blueprint(nologin)
app.register_blueprint(errors)
app.register_blueprint(teste)



from app.utils.flask_mail import mail
mail.init_app(app)


with app.app_context():
    db.create_all()





