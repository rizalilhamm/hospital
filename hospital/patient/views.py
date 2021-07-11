from flask import (
    Blueprint, render_template, flash, url_for, redirect
    )
from flask_login import current_user

from hospital import db


patient_bp = Blueprint(
    'patient', __name__,
    template_folder='templates',
    static_folder='static')

from hospital.models import User, Docter, Appointment

@patient_bp.route('/appointments')
def available_appointment():
    appointments = []
    for appointment in Appointment.query.all():
        appointment_in_dic = {}
        appointment_in_dic['appointment_title'] = appointment.appointment_title
        appointment_in_dic['docter_name'] = Docter.query.get(appointment.docter_id)
        appointment_in_dic['docter_id'] = appointment.docter_id
        appointments.append(appointment_in_dic)

    return render_template('available_appointment.html', title='All Appointments', appointments=appointments)

@patient_bp.route('/docters/<int:docter_id>/<string:appointment_title>/appointment_registration', methods=['GET', 'POST'])
def appointment_registration(docter_id, appointment_title):
    # current_appointment.patients.append(current_patient)
    appointment = Appointment.query.join(Docter.appointments).filter(Docter.docter_id==docter_id).filter_by(appointment_title=appointment_title).first()
    message = 'Appointment registered at: {}'.format(appointment)
    if current_user not in appointment.patients:
        appointment.patients.append(current_user)
    elif current_user in appointment.patients:
        appointment.patients.remove(current_user)
        message = 'Appointment Canceled from: {}'.format(appointment)

    db.session.commit()
    flash(message)
    return redirect((url_for('admin.appointment', docter_id=docter_id, appointment_title=appointment_title)))

@patient_bp.route('/my_appointment/')
def patient_appointment():
    appointments = Appointment.query.join(User.patients).filter(User.email==current_user.email).all()
    return render_template('patient_appointments.html', title='Apppointment ku', appointments=appointments)