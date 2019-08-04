from flask import render_template,Blueprint,redirect,request,session,url_for
from app.models import Usuario,Medico,Adm,CoCriador
from app.utils.flask_mail import redefinir_senha
from app.utils.flask_wtf import formEmail,formLogin

from datetime import datetime
import hashlib

nologin = Blueprint('index', __name__,
                        template_folder='templates')


@nologin.route("/")
def index():
    return redirect('/inicio')

@nologin.route("/inicio")
def inicio():
    if 'tipo' in session:
        if session['tipo']=='paciente':
            redirect('/painel-paciente')
        elif session['tipo']=='medico':
            redirect('/painel-profissional')
        elif session ['tipo']=='adm':
            redirect('/adm')
    coCriadores=CoCriador()
    arr=coCriadores.listar()
    medicos=[]
    for medico in coCriadores:
        id=medico.medico.id
        nome=medico.medico.nome
        descricao=medico.medico.descricao
        foto=medico.medico.foto
        medicos.append({'id':id,"nome":nome,"descricao":descricao,"foto":foto})
    data={'coCriador':medicos}
    return render_template('inicio.jinja',data=data)

@nologin.route("/recuperacao-de-senha",methods = ['GET', 'POST'])
def recuperaSenha():
    form = formEmail()
    erro=None
    if request.method == 'POST':
        if form.validate():
            email=request.form['email']
            busca={'email':str(email)}
            usuario= Usuario.buscaGenerica(busca)
            medico=Medico.buscaGenerica(busca)
            if usuario !=None:
                user=usuario
            elif medico !=None:
                user=medico
            user.codigo_troca_senha=hashlib.sha256(user.email+user.senha)
            user.expiracao=datetime.now()
            datetime.time
            user.inserir()
            redefinir_senha([user.email],user.codigo_troca_senha)
        else:
            erro="Email null"
            return render_template('recuperacaoDeSenha.jinja',form=form,erro=erro)
    return render_template('recuperacaoDeSenha.jinja',form=form,erro=erro)

@nologin.route('/codigo-de-nova-senha/<codigo>')
def atualizaSenha(codigo):
    busca={'codigo':codigo}
    usuario= Usuario.buscaGenerica(busca)
    medico=Medico.buscaGenerica(busca)
    if usuario != None:
        user=usuario
        tipo="paciente"
    elif medico !=None:
        user=medico
        tipo='profisional'
    else:
        #codigo invalido
        pass
    if user.expiracao+3600>datetime.timestamp(datetime.now()):
        session['tipo']=tipo
        session['id']=user.id
    else:
        #codigo expirado
        pass
    if tipo=='usuario':  
        redirect('/troque-sua-senha-usuario')
    elif tipo=='profissional':  
        redirect('/troque-sua-senha-profisional')
    
@nologin.route('/entrar')
def entrar():
    form=formLogin()
    if request.method == 'POST':
        if form.validate:
            busca={'email':request.form['email'],'senha':hashlib.sha256(request.form['senha'])}
            usuario= Usuario.buscaGenerica(busca)
            medico=Medico.buscaGenerica(busca)
            adm=Adm.buscaGenerica(busca)
            if usuario !=None:
                user=usuario
                tipo='paciente'
            elif medico !=None:
                user=medico
                tipo='medico'
            elif adm!=None:
                user=adm
                tipo='adm'
            session['id']=user.id
            session['tipo']=tipo
            
        redirect('/inicio')

    return render_template('entrar.jinja',form=form)

@nologin.routes('/cadastro')
def cadastro():
    return render_template('cadastro.jinja')
'''

/cadastro/paciente{dados do paciente}{
    blueprint:nologin
    template:cadastroPaciente.jinja
    dados:{
        form
    }
}
/cadastro-profissional-de-saude{dados do profissional}{
    blueprint:nologin
    template:cadastroProfissionalDeSaude.jinja
    dados:{
        form
    }
}
'''