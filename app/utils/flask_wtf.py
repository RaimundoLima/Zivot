from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,Form,SubmitField,BooleanField,validators
from wtforms.validators import DataRequired

class form_usuario(FlaskForm):
    nome=StringField("Nome",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")])
    senha=PasswordField("Senha",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")])
    confirma_senha = PasswordField('Repita a senha',[
        validators.EqualTo("senha",message="As senhas devem ser iguais")])
    email=StringField("Email",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
        validators.Email(message="Email invalido")])
    submit = SubmitField('Cadastrar')

class formEmail(FlaskForm):
    email=StringField("Email",[
    validators.InputRequired(message="Campo obrigatorio"),
    validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
    validators.Email(message="Email invalido")])

class formLogin(FlaskForm):
    email=StringField("Email",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
        validators.Email(message="Email invalido")])
    senha=PasswordField("Senha",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")])
