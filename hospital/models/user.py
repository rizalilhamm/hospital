import datetime
import jwt

from hospital import hospital, db, bcrypt

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    admin = db.Column(db.Boolean, default=False)
    appointments = db.relationship('Appointment', backref='user')

    def __init__(self, firstname, lastname, age, email, password, username, admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, hospital.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.username = username
        self.admin = admin

    def encode_token(self, user_id):
        """Generate the Auth token
            return: string """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=2),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                hospital.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_token(auth_token):
        """Decode the auth Token
            param:
                auth_token
            return:
                Integer | String """

        try:
            payload = jwt.decode(auth_token, hospital.config.get('SECRET_KEY'))
            return payload
        except jwt.ExpiredSignatureError:
            return 'Invalid Signature'
        except jwt.InvalidTokenError:
            return 'Invalid token, please log in again!'