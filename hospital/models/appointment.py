from functools import partialmethod
from hospital import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.String(100), nullable=False)
    appointment_desc = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    docter_id = db.Column(db.Integer, db.ForeignKey('docters.docter_id'))
    

    def __init__(self, appointment_title):
        self.appointment_title = appointment_title

    def __repr__(self):
        return "<Appointment title: {}>".format(self.appointment_title)