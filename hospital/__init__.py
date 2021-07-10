from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

hospital = Flask(__name__)
hospital.config.from_object(Config)
db = SQLAlchemy(hospital)
bcrypt = Bcrypt(hospital)

from hospital.auth.views import auth_bp
from hospital.admin.views import admin_bp
from hospital.home.views import home_bp
from hospital.patient.views import patient_bp
from hospital.models import *

hospital.register_blueprint(auth_bp)
hospital.register_blueprint(admin_bp)
hospital.register_blueprint(home_bp)
hospital.register_blueprint(patient_bp)


