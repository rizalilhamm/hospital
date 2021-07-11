
from flask import (
    Blueprint, request, redirect, url_for, flash, render_template, g, session
)
from flask_login import login_user

auth_bp = Blueprint('auth', __name__,
    template_folder='templates', static_folder='static'
    )

from hospital import db, bcrypt
from hospital.models import User


def register(admin):
    if request.method == 'POST':
        firstname = request.form['username']
        lastname = request.form['lastname']
        age = request.form['age']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        arguments = all([firstname.strip(), lastname.strip(), age.strip(), email.strip(), username.strip(), password.strip()])
        if not arguments:
            flash('Semua parameters wajib diisi!')
            return redirect(url_for('auth.admin_register'))
        if password != confirm_password:
            flash('Password harus sama!')
            return redirect(url_for('auth.admin_register'))

        if User.query.filter_by(email=email).first():
            flash('Email sudah terdaftar, silahkan, login')
            return redirect(url_for('auth.admin_login'))
        new_user = User(firstname=firstname, lastname=lastname, 
                        age=age, email=email, username=username, password=password)
        new_user.admin = admin
        db.session.add(new_user)
        db.session.commit()
        user_rule = 'User Biasa'
        if admin:
            user_rule = 'Admin'
        flash('Pendaftaran Berhasil sebagai {}'.format(user_rule))
        return redirect(url_for('auth.login'))

@auth_bp.route('/admin/register/', methods=['POST', 'GET'])
def admin_register():
    register(admin=True)
    return render_template('admin_register.html', title='Admin Register', user_type='ADMIN')

@auth_bp.route('/patient/register/', methods=['POST', 'GET'])
def patient_register():
    register(admin=False)
    return render_template('patient_register.html', title='Register')

@auth_bp.route('/login/', methods=['POST', 'GET'])
def login():
    if session.get('logged_in'):
        if session.get('user_rule'):
            flash('Kamu masih login sebagai Admin!')
            return redirect(url_for('admin.docters'))
        else:
            flash('Kamu masih login sebagai Patient!')
            
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                session['logged_in'] = True
                session['user_admin'] = False
                message = 'Kamu berhasil login sebagai Patient!'
                if user.admin:
                    session['user_admin'] = True
                    message = 'Kamu berhasil login sebagai Admin!'
                
                login_user(user)
                flash(message)
                return redirect(url_for('admin.docters'))
            flash('Password anda salah')
            return redirect(url_for('auth.login'))
        flash('Email tidak ditemukan')
        return redirect(url_for('auth.login'))

    return render_template('login.html', title='Login')

@auth_bp.route('/logout')
def logout():
    session['logged_in'] = None
    session['user_rule'] = None
    flash('Kamu sudah Logout!')
    return redirect(url_for('auth.login'))
