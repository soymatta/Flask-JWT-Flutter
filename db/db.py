from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS for all domains
app.template_folder = "../templates"

app.config.from_object(Config)

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
