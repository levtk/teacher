from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from user.user import UserRegisterForm, User
from db.db import get_user_by_email, insert_user
import os
import logging
import uuid

logging.basicConfig(
    level=logging.INFO,  # Set the default logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


if load_dotenv():
    logger.info('loaded .env file...')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modal')
def modal():
    return render_template('dynamic_modal.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/reg_pending')
def reg_pending():
    return render_template('reg_pending.html')

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
        teacher = get_user_by_email('davenlorena@gmail.com')
        if teacher:
            print(f'The teacher is , {teacher.first_name}')
            new_user = User(first_name=session['first_name'],second_name=session['second_name'],third_name=session['third_name'],fourth_name=session['fourth_name'],
                        email=session['email'],phone=session['phone'], user_type=[2],instructor_id=teacher.id, instructor_name=teacher.first_name, whatsapp=session['whatsapp'], id=str(uuid.uuid4()), subscription_plan=None)
            logger.debug(new_user)
            insert_user(new_user)
            return redirect(url_for('reg_pending'))
        else:
            logger.warn('failed to find teacher by invite_code')
        return redirect(url_for('reg_pending'))
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