from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/dash/contacts')

@contact.route('/')
def index():
    return "dash.contact.index"
