# from typing import str
# from typing import Integer
from flask import Blueprint, render_template  # , Response

contact = Blueprint(
    'contact',
    __name__,
    template_folder="templates",
    url_prefix='/dash/contacts'
)

@contact.route('/')
def index() -> str:
    # return "dash.contact.index"
    return render_template('index.html')

@contact.route('/create')
def create() -> str:
    return "dash.contact.create"

@contact.route('/', methods=['POST'])
def store() -> str:
    return "dash.contact.store"

@contact.route('/<int:id>')
def show(id: int) -> str:
    return f"dash.contact.show {id}"

@contact.route('/<int:id>/edit')
def edit(id: int) -> str:
    return f"dash.contact.edit {id}"

@contact.route('/<int:id>', methods=['PUT'])
def update(id: int) -> str:
    return f"dash.contact.update {id}"

@contact.route('/<int:id>', methods=['DELETE'])
def destroy(id: int) -> str:
    return f"dash.contact.destroy {id}"
