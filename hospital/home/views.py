from flask import Blueprint, render_template

home_bp = Blueprint(
    'home',__name__,
    template_folder='templates'
    )

@home_bp.route('/')
def home():
    return render_template('home.html', title='Home')

@home_bp.route('/about-us/')
def about_us():
    return render_template('about_us.html', title='About Us')

@home_bp.route('/contact-us/')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')