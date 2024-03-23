from datetime import date, datetime
from logging import Logger
from uuid import UUID, uuid4
import uuid
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from user.user import User
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the default logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

load_dotenv()
db = os.getenv("POSTGRES_DB")
db_user = os.getenv('POSTGRES_USER')
db_pw = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("HOST")

def insert_user(user: User):
    """Inserts a user into the users table"""

    sql = """INSERT INTO USERS(id, first_name, second_name, third_name, fourth_name, user_type, email, phone, whatsapp, instructor_name, created, updated, instructor_id) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    conn = psycopg2.connect(database=db,user=db_user,password=db_pw,host=host) 
    record = (str(user.id), user.first_name, user.second_name, user.third_name, user.fourth_name, user.user_type, user.email, user.phone, user.whatsapp, user.instructor_name, date.today(), datetime.now(), user.instructor_id)
    print({}, record)
    psycopg2.extras.register_uuid()
    cursor = conn.cursor()
    
    cursor.execute(sql, record)
    conn.commit()
    conn.close()

def get_user(id: str) -> User:
    """Retrieves a user from the DB using their id"""

    sql = """SELECT * FROM USERS WHERE id = %s"""

    conn = psycopg2.connect(database=db,user=db_user,password=db_pw,host=host) 
    cursor = conn.cursor()
    cursor.execute(sql, id)
    conn.commit()
    conn.close()

def get_user_by_email(email: str) -> User:

    sql = """SELECT first_name, second_name, third_name, fourth_name, user_type, email, phone, whatsapp, instructor_name, id, instructor_id, subscription_plan FROM users WHERE email = %s"""
    
    conn = psycopg2.connect(database=db,user=db_user,password=db_pw,host=host) 
    cursor = conn.cursor()
    cursor.execute(sql, (email,))
    result = cursor.fetchall()
    print('result[0] is {}', result[0])
    conn.close()
    if result:
        user = User(*result[0])
        print("inside db", user.id)
        return user
    else:
        return None
    

def get_instructor_id_by_email(email: str) -> str:

    sql = """SELECT (instructor_id) FROM users WHERE email = %s"""
    
    conn = psycopg2.connect(database=db,user=db_user,password=db_pw,host=host) 
    cursor = conn.cursor()
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    print('result[0] is {}', result[0])
    conn.close()
    if result:
        print("inside db", result[0])
        return result[0]
    else:
        return None

