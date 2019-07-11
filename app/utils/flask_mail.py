from flask_mail import Mail, Message

mail=Mail()

def bem_vindo(recipis):
   msg = Message('Bem vindo a Zivot', recipients = recipis)
   msg.html = "<b>yo mah boy</b> <h3>YEAAAAHH</h3>"
   mail.send(msg)
   return True

def redefinir_senha(recipis):
   pass

def cadastro_aprovado(recipis):
   pass

def aguardando_aprovacao(recipis):
   pass