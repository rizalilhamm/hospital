from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect

from hospital import db
from hospital.models import Appointment


admin_bp = Blueprint('admin', __name__,
    template_folder='templates', static_folder='static')

from hospital.models import Docter, Appointment

@admin_bp.route('/docters', methods=['POST', 'GET'])
def docters():
    """ Show all docters and provide a link to the available appointments """
    docters = Docter.query.all()
    return render_template('all_docters.html', docters=docters)

@admin_bp.route('/docters/<int:docter_id>', methods=['GET', 'POST'])
def appointments(docter_id):
    docter = Docter.query.get(docter_id)
    all_appointments = Appointment.query.filter_by(docter_id=docter_id).all()
    
    if request.method == 'POST':
        appointment_title = request.form['appointment_title']
        appointment_desc = request.form['appointment_desc']
        # appointment_desc = None
        arguments = all([appointment_title, appointment_desc])
        if arguments:
            new_appointment = Appointment(
                appointment_title=appointment_title, 
                appointment_desc=appointment_desc,
                docter_id=docter_id)
        
            db.session.add(new_appointment)
            db.session.commit()
            flash('Appointment berhasil ditambahkan ke docter: {}'.format(docter.name))
            return redirect(url_for('admin.appointments', docter_id=docter.docter_id))
        flash('Semua appointment field wajib diisi')
        return redirect(url_for('admin.appointments', docter_id=docter.docter_id))

    return render_template('docter_appointments.html', docter=docter, all_appointments=all_appointments)