from sqlite3 import Error
import pandas
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, inspect
from flask import Flask, request, render_template, jsonify, session, redirect
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_login import login_required, logout_user, login_user, current_user
from flask_admin import Admin, BaseView, expose, AdminIndexView
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


class adminview(ModelView):
    pass


class Users(UserMixin, db.Model):
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


class Champion(UserMixin, db.Model):
    __tablename__ = 'champion'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Integer)
    lore_id = db.Column(db.Integer)
    championstats_id = db.Column(db.Integer)
    abilityInfo_id = db.Column(db.Integer)
    dmgType = db.Column(db.String(30))

    def __init__(self, id, name, price, lore_id, championstats_id, abilityInfo_id, dmgType):
        self.id = id
        self.name = name
        self.price = price
        self.lore_id = lore_id
        self.championstats_id = championstats_id
        self.abilityInfo_id = abilityInfo_id
        self.dmgType = dmgType


class ChampionStats(UserMixin, db.Model):
    __tablename__ = 'championStats'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    hp = db.Column(db.String(50))
    resource = db.Column(db.String(50))
    healthregen = db.Column(db.String(50))
    manaregen = db.Column(db.String(50))
    armor = db.Column(db.String(50))
    atkdmg = db.Column(db.String(50))
    magicresist = db.Column(db.String(50))
    critdmg = db.Column(db.String(50))
    movespeed = db.Column(db.String(50))
    attackrange = db.Column(db.String(50))
    baseas = db.Column(db.String(50))
    atkwindup = db.Column(db.String(50))
    bonusas = db.Column(db.String(50))
    gameplayradius = db.Column(db.String(50))
    selectionradius = db.Column(db.String(50))
    pathingradius = db.Column(db.String(50))
    acqradius = db.Column(db.String(50))

    def __init__(self, id, champion_id, hp, resource, healthregen, manaregen, armor, atkdmg, magicresist, critdmg, movespeed, attackrange, baseas, atkwindup, bonusas, gameplayradius, selectionradius, pathingradius, acqradius):
        self.id = id
        self.champion_id = champion_id
        self.hp = hp
        self.resource = resource
        self.healthregen = healthregen
        self.manaregen = manaregen
        self.armor = armor
        self.atkdmg = atkdmg
        self.magicresist = magicresist
        self.critdmg = critdmg
        self.movespeed = movespeed
        self.attackrange = attackrange
        self.baseas = baseas
        self.atkwindup = atkwindup
        self.bonusas = bonusas
        self.gameplayradius = gameplayradius
        self.selectionradius = selectionradius
        self.pathingradius = pathingradius
        self.acqradius = acqradius


class ChampionAbilityInfo(UserMixin, db.Model):
    __tablename__ = 'abilityInfo'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    passive = db.Column(db.String(50))
    q = db.Column(db.String(50))
    w = db.Column(db.String(50))
    e = db.Column(db.String(50))
    r = db.Column(db.String(50))

    def __init__(self, id, champion_id, passive, q, w, e, r):
        self.id = id
        self.champion_id = champion_id
        self.passive = passive
        self.q = q
        self.w = w
        self.e = e
        self.r = r


class ChampionSkins(UserMixin, db.Model):
    __tablename__ = 'championSkins'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    chroma = db.Column(db.Integer)
    prestige_edition = db.Column(db.Integer)

    def __init__(self, id, champion_id, name, price, chroma, prestige_edition):
        self.id = id
        self.champion_id = champion_id
        self.name = name
        self.price = price
        self.chroma = chroma
        self.prestige_edition = prestige_edition


class Championlore (UserMixin, db.Model):
    __tablename__ = 'lore'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    description = db.Column(db.String(100))

    def __init__(self, id, champion_id, description):
        self.id = id
        self.champion_id = champion_id
        self.description = description


class Items(UserMixin, db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Role(UserMixin, db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name


admin = Admin(app)
admin.add_view(adminview(Users, db.session))
admin.add_view(adminview(Champion, db.session))
admin.add_view(adminview(ChampionStats, db.session))
admin.add_view(adminview(ChampionAbilityInfo, db.session))
admin.add_view(adminview(ChampionSkins, db.session))
admin.add_view(adminview(Championlore, db.session))
admin.add_view(adminview(Items, db.session))
admin.add_view(adminview(Role, db.session))


@login.user_loader
def load_user(user_id):
    conn = openConnection("data.sqlite")
    sql = """SELECT *
            FROM users
            WHERE users.id == '{}'""".format(user_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    return Users(rows[0], rows[1], rows[2], rows[3], rows[4])


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
