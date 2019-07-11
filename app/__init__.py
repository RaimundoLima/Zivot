from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("configs.cfg")

from app.blueprints.index import index
from app.blueprints.errors import errors

app.register_blueprint(index)
app.register_blueprint(errors)

from app.models.base import db
db.init_app(app)

from app.utils.flask_mail import mail
mail.init_app(app)


with app.app_context():
    db.create_all()





