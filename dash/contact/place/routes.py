from flask import Blueprint, render_template

place = Blueprint(
    'place',
    __name__,
    template_folder="templates",
    url_prefix='/dash/contacts/places'
)

@place.route('/')
def index():
    # return "dash.place.index"
    return render_template('index.html')

