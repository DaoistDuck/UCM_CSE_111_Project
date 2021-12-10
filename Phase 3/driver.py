import pandas
import os
import json
import sqlite3
from sqlite3 import Error
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_login import login_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.helpers import send_from_directory


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
    __tablename__ = 'users'  # -> this line of code syncs data from the sqlite3 database
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
    dmgType = db.Column(db.String(30))

    def __init__(self, id, name, price, dmgType):
        self.id = id
        self.name = name
        self.price = price
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


class ChampionLore (UserMixin, db.Model):
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


class ChampionItems(UserMixin, db.Model):
    __tablename__ = 'champItems'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    items_id = db.Column(db.Integer)

    def __init__(self, id, champion_id, items_id):
        self.id = id
        self.champion_id = champion_id
        self.items_id = items_id


class Role(UserMixin, db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ChampionRole(UserMixin, db.Model):
    __tablename__ = 'champRole'
    id = db.Column(db.Integer, primary_key=True)
    champion_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)

    def __init__(self, id, champion_id, role_id):
        self.id = id
        self.champion_id = champion_id
        self.role_id = role_id


admin = Admin(app)
admin.add_view(adminview(Users, db.session))
admin.add_view(adminview(Champion, db.session))
admin.add_view(adminview(ChampionStats, db.session))
admin.add_view(adminview(ChampionAbilityInfo, db.session))
admin.add_view(adminview(ChampionSkins, db.session))
admin.add_view(adminview(ChampionLore, db.session))
admin.add_view(adminview(Items, db.session))
admin.add_view(adminview(ChampionItems, db.session))
admin.add_view(adminview(Role, db.session))
admin.add_view(adminview(ChampionRole, db.session))


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
        #session.pop('user_id', None)
        userInfo = getUser(user)
        id = userInfo[0]
        pasword = userInfo[1]
        type = userInfo[2]
        tmpUser = load_user(id)
        if(pasword == passs):
            #session['user_id'] = id
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


@ app.route('/user', methods=['POST', 'GET'])
def user():
    if(request.method == 'POST'):
        mode = json.loads(request.data)['mode']
        print(mode)
        conn = openConnection("data.sqlite")
        sql = """"""
        if mode == 'lore':
            championname = json.loads(request.data)['alt']
            sql = """SELECT description
                    FROM lore, champion
                    WHERE champion.id = lore.champion_id
                    AND champion.name = '{}'
                    """.format(championname)
        elif mode == 'champion':
            championname = json.loads(request.data)['alt']
            sql = """SELECT name, price, dmgType
                    FROM champion
                    WHERE champion.name = '{}'
                    """.format(championname)
        elif mode == 'championStats':
            championname = json.loads(request.data)['alt']
            sql = """SELECT hp ,  resource ,  healthregen ,  manaregen ,  armor ,  atkdmg ,  magicresist ,  critdmg ,  movespeed ,  attackrange ,
                baseas ,  atkwindup , bonusas ,  gameplayradius ,  selectionradius ,  pathingradius ,  acqradius
                    FROM champion,championStats
                    WHERE champion.id = championStats.champion_id
                    AND champion.name = '{}'
                    """.format(championname)
        elif mode == 'abilityInfo':
            championname = json.loads(request.data)['alt']
            sql = """SELECT passive, q, w, e, r
                    FROM champion,abilityInfo
                    WHERE champion.id = abilityInfo.champion_id
                    AND champion.name = '{}'
                    """.format(championname)
        elif mode == 'championSkins':
            championname = json.loads(request.data)['alt']
            sql = """SELECT championSkins.name, championSkins.price, championSkins.chroma, championSkins.prestige_edition
                    FROM champion, championSkins
                    WHERE champion.id = championSkins.champion_id
                    AND champion.name = '{}'
                    """.format(championname)
        elif mode == 'items':
            championname = json.loads(request.data)['alt']
            sql = """SELECT items.name
                    FROM champion, items, champItems
                    WHERE champion.id = champItems.champion_id
                    AND items.id = champItems.items_id
                    AND champion.name = '{}'
                    """.format(championname)
        elif mode == 'checkBox':
            listprice = json.loads(request.data)['price']
            listrole = json.loads(request.data)['role']
            listdmgType = json.loads(request.data)['dmgType']
            pricesize = len(listprice)
            rolesize = len(listrole)
            dmgTypesize = len(listdmgType)
            print("listprice size : {}".format(pricesize))
            print("listrole size : {}".format(rolesize))
            print("listdmgType size : {}".format(dmgTypesize))
            if pricesize == 0:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                """
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.dmgType IN('{}')
                                """.format(listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND role.name IN("{}")
                                """.format(listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listrole[0], listdmgType[0])
            elif pricesize == 1:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({})
                                """.format(listprice[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({})
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({})
                                AND role.name IN("{}")
                                """.format(listprice[0], listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({})
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listrole[0], listdmgType[0])
            elif pricesize == 2:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {})
                                """.format(listprice[0], listprice[1])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {})
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {})
                                AND role.name IN("{}")
                                """.format(listprice[0], listprice[1], listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {})
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listrole[0], listdmgType[0])
            elif pricesize == 3:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {})
                                """.format(listprice[0], listprice[1], listprice[2])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {})
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {})
                                AND role.name IN("{}")
                                """.format(listprice[0], listprice[1], listprice[2], listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {})
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listrole[0], listdmgType[0])
            elif pricesize == 4:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {})
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {})
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {})
                                AND role.name IN("{}")
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {})
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listrole[0], listdmgType[0])
            elif pricesize == 5:
                if rolesize == 0:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {}, {})
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listprice[4])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {}, {})
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listprice[4], listdmgType[0])
                else:
                    if dmgTypesize == 0:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {}, {})
                                AND role.name IN("{}")
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listprice[4], listrole[0])
                    else:
                        sql = """SELECT champion.name
                                FROM champion, role, champRole
                                WHERE champion.id = champRole.champion_id
                                AND role.id = champRole.role_id
                                AND champion.price IN({}, {}, {}, {}, {})
                                AND role.name IN("{}")
                                AND champion.dmgType IN('{}')
                                """.format(listprice[0], listprice[1], listprice[2], listprice[3], listprice[4], listrole[0], listdmgType[0])

        df = pandas.read_sql_query(sql, con=conn).to_dict('records')
        print(df)
        return json.dumps(df)
    if(request.method == 'GET'):
        return render_template("website.html")


# https://stackoverflow.com/questions/67204903/adding-a-favicon-to-flask
@ app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.debug = True

    app.run()
