import sqlite3
import pandas
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
                    champion_id INTEGER NOT NULL,
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
                    id INTEGER NOT NULL,
                    champion_id INTEGER NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    price INTEGER NOT NULL,
                    chroma INTEGER NOT NULL,
                    prestige_edition INTEGER NOT NULL)"""  # GOOD I THINK
        _conn.execute(sql)

        sql = """CREATE TABLE championStats (
                    id INTEGER NOT NULL,
                    champion_id INTEGER NOT NULL,
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
                    asratio VARCHAR(50),
                    bonusas VARCHAR(50) NOT NULL,
                    missle_speed VARCHAR(50),
                    gameplayradius VARCHAR(50) NOT NULL,
                    selectionradius VARCHAR(50) NOT NULL,
                    pathingradius VARCHAR(50) NOT NULL,
                    acqradius VARCHAR(50) NOT NULL)"""  # GOOD
        _conn.execute(sql)

        # sql = """CREATE TABLE user (
        #             id INTEGER NOT NULL,
        #             name VARCHAR(100) NOT NULL,
        #             password VARCHAR(100) NOT NULL,
        #             isAdmin INTEGER NOT NULL)"""  # GOOD
        # _conn.execute(sql)

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

        # sql = "DROP TABLE user"
        # _conn.execute(sql)

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
        # from here
        champion = pandas.read_csv(r'data/champion.csv')
        championdf = pandas.DataFrame(champion)
        for row in championdf.itertuples():
            sql = """INSERT INTO champion VALUES(?,?,?,?,?)
                    """
            args = [row.id, row.name, row.price,
                    row.lore_id, row.championstats_id]
            _conn.execute(sql, args)
        # to here

        # from here
        items = pandas.read_csv(r'data/items.csv')
        itemsdf = pandas.DataFrame(items)
        for row in itemsdf.itertuples():

            sql = """INSERT INTO items VALUES(?,?,?)
                    """
            args = [row.id, row.name, row.price]
            _conn.execute(sql, args)
        # to here

        # from here
        champRole = pandas.read_csv(r'data/champRole.csv')
        champRoledf = pandas.DataFrame(champRole)
        for row in champRoledf.itertuples():

            sql = """INSERT INTO champRole VALUES(?,?,?)
                    """
            args = [row.id, row.champion_id, row.role_id]
            _conn.execute(sql, args)
        # to here

        # from here
        role = pandas.read_csv(r'data/role.csv')
        roledf = pandas.DataFrame(role)
        for row in roledf.itertuples():

            sql = """INSERT INTO role VALUES(?,?)
                    """
            args = [row.id, row.role_name]
            _conn.execute(sql, args)
        # to here

        # from here
        champItems = pandas.read_csv(r'data/champItems.csv')
        champItemsdf = pandas.DataFrame(champItems)
        for row in champItemsdf.itertuples():

            sql = """INSERT INTO champItems VALUES(?,?,?)
                    """
            args = [row.id, row.champion_id, row.items_id]
            _conn.execute(sql, args)
        # to here

        # from here
        lore = pandas.read_csv(r'data/lore.csv')
        loredf = pandas.DataFrame(lore)
        for row in loredf.itertuples():

            sql = """INSERT INTO lore VALUES(?,?,?)
                    """
            args = [row.id, row.champion_id, row.description]
            _conn.execute(sql, args)
        # to here

        abilityInfo = pandas.read_csv(r'data/abilityInfo.csv')
        abilityInfodf = pandas.DataFrame(abilityInfo)
        for row in abilityInfodf.itertuples():

            sql = """INSERT INTO abilityInfo VALUES(?,?,?,?,?,?,?)
                    """
            args = [row.id, row.champion_id,
                    row.passive, row.q, row.w, row.e, row.r]
            _conn.execute(sql, args)

        championSkins = pandas.read_csv(r'data/championSkins.csv')
        championSkinsdf = pandas.DataFrame(championSkins)
        for row in championSkinsdf.itertuples():

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [row.id, row.champion_id,
                    row.name, row.price, row.chroma, row.prestige_edition]
            _conn.execute(sql, args)

        championStats = pandas.read_csv(r'data/championStats.csv')
        championStatsdf = pandas.DataFrame(championStats)
        for row in championStatsdf.itertuples():

            sql = """INSERT INTO championStats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """
            args = [row.id, row.champion_id,
                    row.hp, row.hp, row.healthregen,
                    row.manaregen, row.armor, row.atkdmg,
                    row.magicresist, row.critdmg, row.movespeed,
                    row.attackrange, row.baseas, row.atkwindup,
                    row.asratio, row.bonusas, row.missle_speed,
                    row.gameplayradius, row.selectionradius,
                    row.pathingradius, row.acqradius]
            _conn.execute(sql, args)

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
# https://datatofish.com/import-csv-sql-server-python/
