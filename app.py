from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from auth.views import auth_dp
from models import *

app.register_blueprint(auth_dp)


if __name__ == '__main__':
    app.run(debug=True)