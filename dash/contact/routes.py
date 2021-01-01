from flask import Blueprint, render_template

contact = Blueprint(
    'contact',
    __name__,
    template_folder="templates",
    url_prefix='/dash/contacts'
)

@contact.route('/')
def index():
    # return "dash.contact.index"
    return render_template('index.html')
