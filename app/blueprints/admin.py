from flask import render_template,Blueprint,redirect,request,session,url_for
from app.models import Usuario,Medico


adm = Blueprint('paciente', __name__,
                        template_folder='templates')

@adm.before_request()
def beforeRequest():
    if 'tipo' in session:
        if session['tipo']=='adm':
            pass
        else:
            redirect('/inicio')
