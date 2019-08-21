from flask import render_template,Blueprint,redirect,request,session,url_for
from app.models import Usuario,Medico,Adm,CoCriador,Especialidade,Consulta
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
        elif session['tipo']=='profissional':
            redirect('/painel-profissional')
        elif session ['tipo']=='adm':
            redirect('/adm')
    coCriadores=CoCriador().listar()
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
        session['user']=user.toJson()
    else:
        #codigo expirado
        pass
    if tipo=='paciente':  
        redirect('/troque-sua-senha-usuario')
    elif tipo=='profissional':  
        redirect('/troque-sua-senha-profisional')
    
@nologin.route('/entrar',methods = ['GET', 'POST'])
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
                tipo='profissional'
            elif adm!=None:
                user=adm
                tipo='adm'
            session['user']=user.toJson()
            session['tipo']=tipo
            
        redirect('/inicio')

    return render_template('entrar.jinja',form=form)

@nologin.route('/cadastro')
def cadastro():
    return render_template('cadastro.jinja')

@nologin.route('/cadastro/paciente',methods = ['GET', 'POST'])
def cadastro_paciente():
    form=form_usuario()
    if request.method == 'POST':
        if form.validate:
            redirect('/teste')
        redirect('/teste')
    return render_template('cadastroPaciente.jinja',form)
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
@nologin.route('/sair')
def sair():
    session.clear()
    return redirect('/inicio')

@nologin.route('/profissional-de-saude/<int:id>')
def profissionalDeSaude(id):
    profissional=Medico.buscarId(id)
    data={
        'id':profissional.id,
        'nome':profissional.nome,
        'especialidade':profissional.especialidade,
        'cidade':profissional.cidade,
        'estado':profissional.estado,
        'email':profissional.email,
        'celular':profissional.celular,
        'valor':profissional.valor
    }
    return render_template('profissional-de-saude.jinja',data=data)

'''
/profissional-de-saude/{idprofissional}/calendario/{data}
    blueprint:nologin
    dados:{
        datas[31]{
            disponivel
        }
    }
}
'''
@nologin.route('/profissional-de-saude/<id>/buscar-consultas/{<string:data>')
def buscarConsultas(id,data):
    consulta=Consulta()
    consulta.query.filter(id_medico=id).filter(hora_inicio<data)
    pass
'''
/profissional-de-saude/{idprofissional}/buscar-consultas/{data}{
    blueprint:nologin
    dados:{
        datas{
            datas[todas]{
                online,
                hoarioInicio,
                horariofim
            }
        }
    }
}
'''