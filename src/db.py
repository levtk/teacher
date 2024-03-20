from datetime import date, datetime
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from user import User


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
    record = (user.id, user.first_name, user.second_name, user.third_name, user.fourth_name, user.user_type, user.email, user.phone, user.whatsapp, user.instructor_name, date.today(), datetime.now(), user.instructor_id)
    cursor = conn.cursor()
    psycopg2.extras.register_uuid()
    cursor.execute(sql, record)
    conn.commit()
    conn.close()

def get_user(id: str) -> User:
    """Retrieves a user from the DB using their id"""

    sql = """SELECT * FROM USERS WHERE ID = %s"""

    conn = psycopg2.connect(database=db,user=db_user,password=db_pw,host=host) 
    cursor = conn.cursor()
    cursor.execute(sql, id)
    result = cursor.fetchall()
    print(result)
    conn.close()
    

