from flask import Flask
from dash.contact import routes as contact_routes
from dash.contact.place import routes as contact_place_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(contact_routes.contact)
    app.register_blueprint(contact_place_routes.place)

    @app.route('/dash/')
    def hello():
        return 'Dash'
    
    return app