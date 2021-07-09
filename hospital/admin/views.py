from flask import Blueprint, render_template, request

admin_bp = Blueprint('admin', __name__,
    template_folder='templates', static_folder='static')

from hospital.models import Docter, Appointment

@admin_bp.route('/docters', methods=['POST', 'GET'])
def docters():
    docters = Docter.query.all()
    return render_template('home.html', docters=docters)

