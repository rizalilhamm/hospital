from functools import partialmethod

from sqlalchemy.sql.operators import nullslast_op
from hospital import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.String(100), nullable=False)
    appointment_desc = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    docter_id = db.Column(db.Integer, db.ForeignKey('docters.docter_id'))
    

    def __init__(self, appointment_title, appointment_desc, docter_id):
        self.appointment_title = appointment_title
        self.appointment_desc = appointment_desc
        self.docter_id = docter_id

    def __repr__(self):
        return self.appointment_title