from flask import render_template,Blueprint

index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route("/")
def home():
    return render_template('painel.jinja')

