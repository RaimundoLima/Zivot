from flask import render_template,Blueprint,redirect,request,session,url_for

notificacao = Blueprint('notificacao',__name__,
                        template_folder='templates')

@notificacao.routes('/visualizar-notificacoes')
def visualizarNotificacoes():
    pass

@notificacao.routes('/atualizar-notificacoes')
def atualizarNotificacoes():
    pass

@notificacao.routes('/notificacoes')
def notificacoes():
    return render_template('notificacao.html')
'''
/visualizar-notificacoes{
    blueprint:notificacao
    //visualiza todas as notificações do usuario logado
}
/atualizar-notificacoes{
    blueprint:notificacao
    dados:{
        notificacoes[10]{
            id,
            texto,
            dateTime        
        }
    }
}
/notificacoes{
    blueprint:notificacao
    template:notificacoes.html
    dados:{
        notificacoes[todas]{
            id,
            texto,
            dateTime        
        }
    }
}
'''

