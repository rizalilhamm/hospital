from flask import Blueprint, render_template


patient_bp = Blueprint(
    'patient', __name__,
    template_folder='templates',
    static_folder='static')

from hospital.models import Docter, Appointment

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