
import code # to debug: `code.interact(local=locals())`
import os
from flask import Flask, render_template #request, session, g, redirect, url_for, abort, flash
from flaskext.mysql import MySQL # https://github.com/cyberdelia/flask-mysql

#
# INITIALIZE AND CONFIGURE NEW FLASK APPLICATION
#

try:
    DB_ROOT_PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"] # if your root user has a password, assign it to the "MYSQL_ROOT_PASSWORD" environment variable
except KeyError as e:
    DB_ROOT_PASSWORD = "" # most students' root user doesn't have a password

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = DB_ROOT_PASSWORD
app.config['MYSQL_DATABASE_DB'] = 'salad_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

#
# DEFINE ROUTES
#

@app.route("/")
def hello():
    return "<h1>Welcome, Regional Manager.</h1><a href='/menu'>View Menu</a>"

@app.route("/menu")
def menu():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from menu_items ORDER BY id LIMIT 10;")
    menu_items = [dict(title=row[2], description=row[6]) for row in cursor.fetchall()]
    return render_template('menu.html', menu_items=menu_items)


















if __name__ == "__main__":
    app.debug = True
    app.run()
