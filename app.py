from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from auth.views import auth_dp
from admin.views import admin_bp
from models import *

app.register_blueprint(auth_dp)
app.register_blueprint(admin_bp)


if __name__ == '__main__':
    app.run(debug=True)