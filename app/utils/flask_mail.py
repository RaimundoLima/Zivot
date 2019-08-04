from flask_mail import Mail, Message

mail=Mail()

def bem_vindo(recipis):
   msg = Message('Bem vindo a Zivot', recipients = recipis)
   msg.html = "<b>yo mah boy</b> <h3>YEAAAAHH</h3>"
   mail.send(msg)
   return True

def redefinir_senha(recipis,codigo):
   msg = Message('trocou senha', recipients = recipis)
   msg.html = "<b>Acesse esse link</b> http://127.0.0.1:5000/codigo/"+str(codigo)
   mail.send(msg)
   return True

def cadastro_aprovado(recipis):
   pass

def aguardando_aprovacao(recipis):
   pass