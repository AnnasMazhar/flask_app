# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

bootstrap = Bootstrap()

def create_app(config_type): # dev, prod, staging
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # / home / stackweavers / Desktop / Workspace / book_catalog / config / dev.py
    app.config.from_pyfile(configuration)

    db.init_app(app)    # bind dtatabase to flask app

    bootstrap.init_app(app)     #initialize bootstrap

    from app.catalog import main   # import blyueprint

    app.register_blueprint(main)   # using blueprint

    return app
