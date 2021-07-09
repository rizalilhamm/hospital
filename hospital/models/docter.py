from sqlalchemy.orm import backref
from hospital import db

class Docter(db.Model):
    __tablename__ = 'docters'
    docter_id = db.Column( db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    appointments = db.relationship('Appointment', backref='docter', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
