from flask import render_template,Blueprint,redirect
from app.models import Especialidade
from datetime import datetime
import json

teste = Blueprint('teste', __name__,template_folder='templates')

@teste.route("/teste", methods=["GET", "POST"])
def testes():
    esp=Especialidade(nome="medico 2")
    medico2="medico trol"
    busca={'nome':str(medico2)}
    yo=[]
    yo.append(esp.buscaGenerica(busca))
    yo.append(esp.buscaGenerica(busca))
    yo=json.dumps(list(map(lambda x:x.as_dict(),yo)),default=str)

    return str(yo)