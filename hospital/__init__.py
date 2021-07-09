from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

hospital = Flask(__name__)
hospital.config.from_object(Config)
db = SQLAlchemy(hospital)
bcrypt = Bcrypt(hospital)

from hospital.auth.views import auth_dp
from hospital.admin.views import admin_bp
from hospital.models import *

hospital.register_blueprint(auth_dp)
hospital.register_blueprint(admin_bp)

