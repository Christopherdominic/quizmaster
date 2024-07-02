from flask import render_template, flash, redirect, url_for, Blueprint
from app import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def home():
    return render_template('index.html', title='Home')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Sign In', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

