from flask_wtf import FlaskForm
from wtforms import DateField,StringField,PasswordField,Form,SubmitField,BooleanField,validators,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired

class form_usuario(FlaskForm):
    style = {'class':'form-control'}
    
    nome=StringField("Nome",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")],render_kw=style)

    senha=PasswordField("Senha",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")],render_kw=style)

    confirma_senha = PasswordField('Repita a senha',[
        validators.EqualTo("senha",message="As senhas devem ser iguais")],render_kw=style)

    email=StringField("Email",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
        validators.Email(message="Email invalido")],render_kw=style)

    celular=IntegerField('Celular',[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    sexo=SelectField(
        'Sexo',
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não Binario', 'Não Binario')],render_kw=style)

    def validate_sexo(self, field):
        if field.data =="Masculino" or field.data == "Feminino" or field.data=="Não Binario":
            pass
        else:
            raise ValidationError('sexo invalido')

    nascimento=DateField('Data de nascimento',[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    cpf=StringField('CPF',[validators.InputRequired(message="Campo obrigatrio")],render_kw={'class':'form-control'})
    def validate_cpf(self,field):
        pass
    estado=SelectField('Estado',choices=[],render_kw=style)##ancap
    def validate_estado(self,field):
        pass
    cidade=SelectField('Cidade',choices=[],render_kw=style)##ancap
    def validate_cidade(self,field):
        pass

    cep=StringField("CEP",[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    bairro=StringField("Bairro",[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    rua=StringField("Rua",[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    numero=IntegerField('Numero',[validators.InputRequired(message="Campo obrigatorio")],render_kw=style)

    complemento=StringField("Complemento",render_kw=style)

    receber_noticias=BooleanField("Receber noticias")

    submit = SubmitField('Cadastrar',render_kw={'class':'btn btn-primary'})

class formMedico(FlaskForm):
    pass

class formEmail(FlaskForm):
    style = {'class':'form-control'}
    email=StringField("Email",[
    validators.InputRequired(message="Campo obrigatorio"),
    validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
    validators.Email(message="Email invalido")],render_kw=style)


class formAvaliacao(FlaskForm):
    style = {'type':'hidden'}
    style2 = {'class':'form-control', 'rows':'3'}
    nota=BooleanField('Nota', render_kw=style)
    descricao=StringField("Descrição", render_kw=style2)
    denuncia=BooleanField("É uma denuncia")
    falta=BooleanField("Paciente faltou")



class formLogin(FlaskForm):
    style = {'class':'form-control'}
    email=StringField("Email",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres"),
        validators.Email(message="Email invalido")],render_kw=style)
    senha=PasswordField("Senha",[
        validators.InputRequired(message="Campo obrigatorio"),
        validators.Length(min=3,max=50,message="O nome deve ter entre 3 e 50 caracteres")],render_kw=style)
