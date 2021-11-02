import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")

    try:

        sql = """CREATE TABLE champion (
                    id INTEGER NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    price INTEGER NOT NULL,
                    lore_id INTEGER NOT NULL,
                    championstats_id INTEGER NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE champItems (
                    id INTEGER NOT NULL,
                    champion_id INTEGER NOT NULL,
                    items_id INTEGER NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE champRole (
                    id INTEGER NOT NULL,
                    champion_id INTEGER NOT NULL,
                    role_id INTEGER NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE role (
                    id INTEGER NOT NULL,
                    role_name VARCHAR(50) NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE items (
                    id INTEGER NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    price INTEGER NOT NULL)"""  # GOOD FOR NOW, DECIDE IF WE NEED STATS LATER?
        _conn.execute(sql)

        sql = """CREATE TABLE lore (
                    id INTEGER NOT NULL,
                    description VARCHAR(1000) NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE abilityInfo (
                    id INTEGER NOT NULL,
                    champion_id INTEGER NOT NULL,
                    passive VARCHAR(1000) NOT NULL,
                    q VARCHAR(1000) NOT NULL,
                    w VARCHAR(1000) NOT NULL,
                    e VARCHAR(1000) NOT NULL,
                    r VARCHAR(1000) NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE championSkins (
                    champion_id INTEGER NOT NULL,
                    id INTEGER NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    price INTEGER NOT NULL,
                    chroma VARCHAR(50) NOT NULL)"""  # GOOD I THINK
        _conn.execute(sql)

        sql = """CREATE TABLE championStats (
                    id INTEGER NOT NULL,
                    hp VARCHAR(50) NOT NULL,
                    resource VARCHAR(50) NOT NULL,
                    healthregen VARCHAR(50) NOT NULL,
                    manaregen VARCHAR(50) NOT NULL,
                    armor VARCHAR(50) NOT NULL,
                    atkdmg VARCHAR(50) NOT NULL,
                    magicresist VARCHAR(50) NOT NULL,
                    critdmg VARCHAR(50) NOT NULL,
                    movespeed VARCHAR(50) NOT NULL,
                    attackrange VARCHAR(50) NOT NULL,
                    baseas VARCHAR(50) NOT NULL,
                    atkwindup VARCHAR(50) NOT NULL,
                    asratio VARCHAR(50) NOT NULL,
                    bonusas VARCHAR(50) NOT NULL,
                    gameplayradius VARCHAR(50) NOT NULL,
                    selectionradius VARCHAR(50) NOT NULL,
                    pathingradius VARCHAR(50) NOT NULL,
                    acqradius VARCHAR(50) NOT NULL)"""  # GOOD
        _conn.execute(sql)

        sql = """CREATE TABLE user (
                    id INTEGER NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    isAdmin INTEGER NOT NULL)"""  # GOOD
        _conn.execute(sql)

        # sql = """CREATE TABLE userRole (
        #             id INTEGER NOT NULL,
        #             user_id INTEGER NOT NULL)"""  #COME BACK TO THIS AT LATER TIME
        # _conn.execute(sql)

        # sql = """CREATE TABLE role (
        #             role_id INTEGER NOT NULL,
        #             role_name VARCHAR(100) NOT NULL)"""  # FILL IN LATER
        # _conn.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = "DROP TABLE champion"
        _conn.execute(sql)

        sql = "DROP TABLE champItems"
        _conn.execute(sql)

        sql = "DROP TABLE champRole"
        _conn.execute(sql)

        sql = "DROP TABLE role"
        _conn.execute(sql)

        sql = "DROP TABLE lore"
        _conn.execute(sql)

        sql = "DROP TABLE items"
        _conn.execute(sql)

        sql = "DROP TABLE abilityInfo"
        _conn.execute(sql)

        sql = "DROP TABLE user"
        _conn.execute(sql)

        # sql = "DROP TABLE UserRole"
        # _conn.execute(sql)

        # sql = "DROP TABLE Role"
        # _conn.execute(sql)

        sql = "DROP TABLE championSkins"
        _conn.execute(sql)

        sql = "DROP TABLE championStats"
        _conn.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Tables")
    try:
        sql = """INSERT INTO champion VALUES(1,"Aatrox",4800,1,1)"""
        _conn.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populateTables(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()

# A lot of the code is modified from the code given to us by the professor in Lecture 22 ODBC-Python SQLite.py
