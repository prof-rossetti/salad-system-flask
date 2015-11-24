
import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
import os
from flask import Flask #, render_template, request, session, g, redirect, url_for, abort, flash
from flaskext.mysql import MySQL # https://github.com/cyberdelia/flask-mysql

try:
    DB_ROOT_PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"] # if your root user has a password, assign it to the "MYSQL_ROOT_PASSWORD" environment variable
except KeyError as e:
    DB_ROOT_PASSWORD = "" # most students' root user doesn't have a password

app = Flask(__name__)
app.secret_key = os.urandom(24) # to facilitate sessions and flash
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = DB_ROOT_PASSWORD
app.config['MYSQL_DATABASE_DB'] = 'salad_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

def create_menu_item():
    connection = mysql.connect()
    cursor = connection.cursor()
    sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`gluten_free`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
    print(sql)
    cursor.execute(sql, ('SignatureSalad', 'TEST SALAD',  1111, 0, 1,  'a salad to use when testing the web application.'))
    connection.commit()

def count_menu_items():
    cursor = mysql.connect().cursor()
    sql = "SELECT * FROM menu_items;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)

create_menu_item()

count_menu_items()
