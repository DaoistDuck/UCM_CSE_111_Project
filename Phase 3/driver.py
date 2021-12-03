from sqlite3 import Error
import pandas
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, inspect
from flask import Flask, request, render_template, jsonify, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_login import login_required, logout_user, login_user, current_user
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.secret_key = 'ASDASDDASDSAFA'
login = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# The open and close connection code is taken from the python files from the CSE 111 Labs


def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn


def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

# https://python-adv-web-apps.readthedocs.io/en/latest/flask_db2.html


class User(UserMixin, db.Model):
    __tablename__ = 'users'  # -> this 1 line of code enluded me for so long
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    types = db.Column(db.String(30))

    def __init__(self, id, name, username, password, types):
        self.username = username
        self.password = password
        self.name = name
        self.types = types
        self.id = id


class adminview(ModelView):
    pass


# class studentview(ModelView):
#     pass


# class Teacherview(ModelView):
#     pass

admin = Admin(app)
admin.add_view(adminview(User, db.session))


@login.user_loader
def load_user(user_id):
    conn = openConnection("data.sqlite")
    sql = """SELECT *
            FROM users
            WHERE users.id == '{}'""".format(user_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    return User(rows[0], rows[1], rows[2], rows[3], rows[4])


def getUser(user):
    conn = openConnection("data.sqlite")
    sql = """SELECT users.id, users.password, users.types
            FROM users
            WHERE users.username == '{}'""".format(user)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    rowInfo = []
    for row in rows:
        rowInfo.append(row[0])
        rowInfo.append(row[1])
        rowInfo.append(row[2])
    return rowInfo


@ app.route('/', methods=['GET', 'POST'])
def login():
    user = "tmp"
    passs = "tmp"
    if(request.method == "POST"):
        user = request.form['username']
        passs = request.form['password']

    try:
        session.pop('user_id', None)
        userInfo = getUser(user)
        id = userInfo[0]
        pasword = userInfo[1]
        type = userInfo[2]
        tmpUser = load_user(id)
        if(pasword == passs):
            session['user_id'] = id
            login_user(tmpUser)
            if(type == 1):
                print("ADMIN")
                return redirect('admin')
            if(type == 2):
                print("USER")
                return redirect("/user")
        else:
            print("FAIL")
    except:
        print("User does not exist")
    return render_template("login.html")


@ app.route('/user', methods=['GET'])
def user():
    if(request.method == 'GET'):
        return render_template("website.html")


if __name__ == '__main__':
    app.debug = True

    app.run()
