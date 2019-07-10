from flask import render_template,Blueprint

errors = Blueprint('errors', __name__,
                        template_folder='templates')

@errors.app_errorhandler(404)
def error(error):
	return '404 nof found',404

@errors.app_errorhandler(500)
def error(error):
	return 'Erro interno',500