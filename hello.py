
import code # to debug: `code.interact(local=locals())`
import os
from flask import Flask
from flaskext.mysql import MySQL # https://github.com/cyberdelia/flask-mysql

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

@app.route("/")
def hello():
    return "<h1>Welcome, Regional Manager.</h1><a href='/menu'>View Menu</a>"

@app.route("/menu")
def menu():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from menu_items ORDER BY id LIMIT 10;")

    menu_item_list = "<ul>"
    for row in cursor.fetchall():
        print(row)
        #code.interact(local=locals())
        #menu_item_list = menu_item_list + "<li>" + row["title"] + " - " + row["description"] + "</li>"
        menu_item_list = menu_item_list + "<li>" + row[2] + " - " + row[6] + "</li>"

    menu_item_list += "</ul>"
    return menu_item_list



















if __name__ == "__main__":
    app.run()
