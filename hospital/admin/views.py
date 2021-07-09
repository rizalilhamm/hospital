from flask import Blueprint, render_template, request, flash, session
from flask.helpers import url_for
from werkzeug.utils import redirect

from hospital import db
from hospital.models import Docter, Appointment


admin_bp = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static'
    )

from hospital.models import Docter, Appointment


@admin_bp.route('/docters/', methods=['POST', 'GET'])
def docters():
    """ Show all docters and provide a link to the available appointments """
    docters = Docter.query.all()
    return render_template('all_docters.html', docters=docters)


@admin_bp.route('/docters/<int:docter_id>/', methods=['GET', 'POST'])
def appointments(docter_id):
    """Show all partocular docter appointments from
    param:
        docter_id(int)
    return:
        all docter appoinment"""
    docter = Docter.query.get(docter_id)
    all_appointments = Appointment.query.filter_by(docter_id=docter_id).all()
    
    if request.method == 'POST' and session['user_admin']:
        appointment_title = request.form['appointment_title']
        appointment_desc = request.form['appointment_desc']
        arguments = all([appointment_title, appointment_desc])
        if arguments:
            new_appointment = Appointment(
                appointment_title=appointment_title, 
                appointment_desc=appointment_desc,
                docter_id=docter_id)
        
            db.session.add(new_appointment)
            db.session.commit()
            flash('{} berhasil ditambahkan ke docter: {}'.format(appointment_title.capitalize(), docter.name))
            return redirect(url_for('admin.appointments', docter_id=docter.docter_id))
        flash('Semua appointment field wajib diisi')
        return redirect(url_for('admin.appointments', docter_id=docter.docter_id))

    return render_template('docter_appointments.html', title='All Docters', docter=docter, all_appointments=all_appointments)


@admin_bp.route('/docters/<int:docter_id>/<string:appointment_title>', methods=['GET', 'PUT'])
def appointment(docter_id, appointment_title):
    """Function will show us the Appointment detail"""
    appointment = Appointment.query.join(Docter.appointments).filter(Docter.docter_id==docter_id).filter_by(appointment_title=appointment_title).first()
    return render_template('appointment_detail.html', title='Appointment', appointment=appointment, docter=Docter.query.get(docter_id))


@admin_bp.route('/docters/<int:docter_id>/<string:appointment_title>/update_detail', methods=['GET', 'POST'])
def update_appointment(docter_id, appointment_title):
    """Update the Appointment Detail"""
    docter = Docter.query.get(docter_id)
    appointment = Appointment.query.join(Docter.appointments).filter(Docter.docter_id==docter_id).filter_by(appointment_title=appointment_title).first()
    if request.method == 'POST':
        validate_diff = (appointment.appointment_title != request.form['appointment_title']) or (appointment.appointment_desc != request.form['appointment_desc'])
        if validate_diff:
            appointment.appointment_title = request.form['appointment_title']
            appointment.appointment_desc = request.form['appointment_desc']
        
            db.session.commit()
            flash('Perubahan berhasil disimpan!')
            return redirect(url_for('admin.appointment', docter_id=docter.docter_id, appointment_title=appointment.appointment_title))
        else:
            flash('Tidak ada perubahan yang dilakukan!')
            return redirect(url_for('admin.appointment', docter_id=docter.docter_id, appointment_title=appointment.appointment_title))

    return render_template('update_appointment.html', docter=docter, appointment=appointment)


@admin_bp.route('/docters/<int:docter_id>/<int:appointment_id>/confirmation', methods=['GET', 'POST'])
def confirm_delete(docter_id, appointment_id):
    docter = Docter.query.get(docter_id)
    appointment = Appointment.query.get(appointment_id)
    if request.method == 'POST':
        db.session.delete(appointment)
        db.session.commit()
        flash('{} telah dihapus dari daftar appointment docter {}'.format(appointment.appointment_title.capitalize(), docter))
        return redirect(url_for('admin.appointments',docter_id=docter.docter_id))

    return render_template(
        'confirm_delete.html',
        docter=docter,
        appointment=appointment,
        title='Confirm Delete')
