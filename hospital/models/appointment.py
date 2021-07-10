from enum import unique
from functools import partialmethod

from sqlalchemy.sql.operators import nullslast_op
from hospital import db


patient_identifier = db.Table(
    'patient_identifier',
    db.Column('appointment_id', db.Integer, db.ForeignKey('appointments.appointment_id')),
    db.Column('patient_id', db.Integer, db.ForeignKey('users.user_id'))
)


class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.String(100), unique=True, nullable=False)
    appointment_desc = db.Column(db.Text, nullable=False)
    max_patient = db.Column(db.Integer, default=10)
    docter_id = db.Column(db.Integer, db.ForeignKey('docters.docter_id'))
    patients = db.relationship('User', secondary=patient_identifier)
    

    def __init__(self, appointment_title, appointment_desc, docter_id, max_patient):
        self.appointment_title = appointment_title
        self.appointment_desc = appointment_desc
        self.docter_id = docter_id
        self.max_patient = max_patient

    def __repr__(self):
        return self.appointment_title