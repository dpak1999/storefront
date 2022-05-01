import imp
from flask import Flask
from storefront.config import configurations
from storefront.extension import db


def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    db.init_app(app)
    return app
