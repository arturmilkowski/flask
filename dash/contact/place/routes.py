from flask import Blueprint

place = Blueprint('place', __name__, url_prefix='/dash/contacts/places')

@place.route('/')
def index():
    return "dash.place.index"
