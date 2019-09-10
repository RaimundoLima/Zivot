from flask import render_template,Blueprint,redirect,request,session,url_for
from app.models import Usuario,Medico,Consulta


paciente = Blueprint('paciente', __name__,
                        template_folder='templates')

@paciente.before_request()
def beforeRequest():
    if 'tipo' in session:
        if session['tipo']=='paciente':
            pass
        else:
            redirect('/inicio')

@paciente.route("/saldo-em-conta")
def saldoEmConta():
    return render_template('/saldo-em-conta.jinja')

@paciente.route('solicitar-deposito')
def solicitarDeposito():
    return render_template('solicitarDeposito.jinja')#?

@paciente.route('painel-paciente')
def painelPaciente():
    #definir estados FUK
    consultas = Consulta()
    return render_template('painelPaciente.jinja')

@paciente.route('/minhas-consultas')
def minhasConsultas():
    pass

@paciente.route('/remarcar-consulta/<idConsulta>')
def painelPaciente(idConsulta):
    consulta=Consulta().buscarId(idConsulta)
    data={'consulta':
    {'id':consulta.id,
    'nomeProfissional':consulta.id_medico.nome,
    'online':consulta.online,
    'dateInicio':consulta.horario_inicio,
    'dateFim':consulta.horario_fim}}

    return render_template('remarcarConsulta.jinja',data=data)

@paciente.route('/cancelar-consulta/<idConsulta>')
def cancelarConsulta(idConsulta):
    consulta=Consulta.buscarId(idConsulta)
    consulta.status='aaaa'#definir statuus
    pass
'''
/cancelar-consulta/{idconsulta}{
    blueprint:paciente
    //cancela consulta
}
/avaliar-consulta/{idconsulta}{
    blueprint:paciente
    //avaliação da consulta
}
/editar-perfil-paciente{
    blueprint:paciente
    template:editarPerfil.jinja
    dados:{
        usuario{
            celular,
            estado,
            cidade,
            receberNotificacoes
        }
        form
    }
}
/troque-sua-senha-usuario{senha}{novaSenha}{
    blueprint:paciente
    //troca a senha e envia por email
    dados:{
        form
    }
}

/solicitar-remarcar-consulta-paciente/{idconsulta}/{dateTime}{
    blueprint:paciente
    //
}

'''