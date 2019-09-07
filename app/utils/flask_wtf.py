from flask_wtf import FlaskForm
from wtforms import DateField,StringField,PasswordField,Form,SubmitField,BooleanField,validators,IntegerField
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
    celular=IntegerField('celular',
        validators.InputRequired())
    sexo=SelectField(
        'Sexo',
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não Binario', 'Não Binario')])

    def validate_sexo(self, field):
        if field.data =="Masculino" or field.data == "Feminino" or field.data=="Não Binario":
            pass
        else:
            raise ValidationError('sexo invalido')

    nascimento=DateField('Nascimento',
        validators.InputRequired()),
    cpf=StringField('CPF',validators.InputRequired()),
    def validate_cpf(self,field):
        pass
    estado=SelectField('Estado',choices=[]),##ancap
    def validate_estado(self,field):
        pass
    cidade=SelectField('Cidade',choices=[]),##ancap
    def validate_cidade(self,field):
        pass
    cep=StringField("CEP",validators.InputRequired()),
    bairro=StringField("Bairro",validators.InputRequired()),
    rua=StringField("Rua",validators.InputRequired()),
    numero=IntegerField('Numero',validators.InputRequired()),
    complemento=StringField(),
    receber_noticias=BooleanField(),


    submit = SubmitField('Cadastrar')

class formMedico(FlaskForm):
    pass

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
