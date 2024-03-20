from uuid import uuid4
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from user import UserRegisterForm, User, UserType
from db import insert_user
import os
import logging


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/request/test')
def req():
    ua = request.headers.get('User-Agent')
    return '<h1>Your browser is {}.'.format(ua)

@app.route('/register', methods=['GET','POST'])
def login():
    form = UserRegisterForm()
    if form.validate_on_submit():
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('It looks like you are using a different email than your previous session')
        session['email'] = form.email.data
        session['first_name'] = form.first_name.data
        session['second_name'] = form.second_name.data
        session['third_name'] = form.third_name.data
        session['fourth_name'] = form.fourth_name.data
        session['invite_code'] = form.invite_code.data
        session['phone'] = form.phone.data
        session['whatsapp'] = form.whatsapp.data
        uuid = uuid4()
        new_user = User(first_name=session['first_name'],second_name=session['second_name'],third_name=session['third_name'],fourth_name=session['fourth_name'],
                        email=session['email'],phone=session['phone'], user_type=[2],instructor_id=uuid, instructor_name='valeria', whatsapp=session['whatsapp'], id=uuid)
        logging.debug(new_user)
        insert_user(new_user)
        return redirect(url_for('index')) #TODO create a registration request page informing it's pending.
    return render_template('register.html', form=form)

@app.route('/homework')
def homework():
    return render_template("homework.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500