from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from dotenv import load_dotenv
from user import UserForm
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap(app)
moment = Moment(app)

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('It looks like you are using a different email than your previous session')
        session['email'] = form.email.data
        session['first_name'] = form.first_name.data
        session['second_name'] = form.second_name.data
        session['third_name'] = form.third_name.data
        return redirect(url_for('index')) #TODO create a registration request page informing it's pending.
    return render_template('login.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500