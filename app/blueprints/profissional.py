from flask import render_template,Blueprint,redirect,request,session,url_for
from app.models import Medico


paciente = Blueprint('paciente', __name__,
                        template_folder='templates')

@paciente.before_request()
def beforeRequest():
    if 'tipo' in session:
        if session['tipo']=='profissional':
            pass
        else:
            redirect('/inicio')
