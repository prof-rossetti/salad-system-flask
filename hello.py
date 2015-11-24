
import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
import os
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
from flaskext.mysql import MySQL # https://github.com/cyberdelia/flask-mysql

#
# INITIALIZE AND CONFIGURE NEW FLASK APPLICATION
#

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

#
# DEFINE ROUTES
#

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/menu")
def menu_items():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from menu_items ORDER BY id DESC LIMIT 10;")
    menu_items = [
        dict(
            id= row[0],
            category=row[1],
            title=row[2],
            calories=row[3],
            gluten_free=row[4],
            vegan_safe=row[5],
            description=row[6]
        ) for row in cursor.fetchall()
    ]
    return render_template('menu-items/index.html', menu_items=menu_items)

@app.route("/form")
def edit_menu_item():
    return render_template('menu-items/form.html')

@app.route("/new", methods=['POST'])
def new_menu_item():

    # CAPTURE, VALIDATE, AND TRANSFORM FORM DATA

    category = request.form['category']
    title = request.form['title']
    description = request.form['description']

    try:
        calories = request.form['calories']
        calories = int(calories)
    except ValueError as e:
        #calories = None
        flash('Please specify number of calories.') # A VALIDATION!
        return redirect(url_for('edit_menu_item')) #todo: retain previous form input values instead of resetting the form state

    try:
        gluten_free = True if request.form['gluten_free'] else False
    except KeyError as e:
        gluten_free = False
    finally:
        gluten_free = int(gluten_free)

    try:
        vegan_safe = True if request.form['vegan_safe'] else False
    except KeyError as e:
        vegan_safe = False
    finally:
        vegan_safe = int(vegan_safe)

    # CREATE NEW RECORD

    connection = mysql.connect()
    cursor = connection.cursor()
    sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`gluten_free`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (category, title, calories, gluten_free, vegan_safe, description))
    connection.commit()

    # REDIRECT WITH AN ALERT MESSAGE

    flash('Thanks for adding a menu item.')
    return redirect(url_for('menu_items'))







if __name__ == "__main__":
    app.debug = True
    app.run()
