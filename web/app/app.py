from flask import Flask
from . import views
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar('APP_CONFIG_FILE')

# db setup
db = SQLAlchemy(app)

from .models import Face_Image, Analysis


app.add_url_rule('/', view_func=views.home)
