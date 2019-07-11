from flask import render_template,Blueprint
from app.utils.flask_mail import welcome

index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route("/")
def home():
    
    return render_template('home.jinja')
    

