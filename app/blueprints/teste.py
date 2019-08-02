from flask import render_template,Blueprint,redirect


teste = Blueprint('teste', __name__,template_folder='templates')

@teste.route("/teste", methods=["GET", "POST"])
def testes():
    from app.utils.flask_wtf import form_usuario
    form=form_usuario()
    if form.validate_on_submit():
        return 'aww yeah'
    return render_template('teste.jinja',form=form)