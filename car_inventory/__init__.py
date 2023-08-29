from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db

# Load env variables
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

# Initialize db
root_db.init_app(app)

# Migrate 
migrate = Migrate(app, root_db)