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
                    championstats_id INTEGER NOT NULL,
                    abilityinfo_id INTEGER NOT NULL,
                    dmgType VARCHAR(50) NOT NULL)"""  # GOOD
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
                    bonusas VARCHAR(50) NOT NULL,
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
            print(row)
            sql = """INSERT INTO champion VALUES(?,?,?,?,?,?,?)
                    """
            args = [row.id, row.name, row.price,
                    row.lore_id, row.championstats_id, row.abilityinfo_id, row.dmgType]
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

            sql = """INSERT INTO championStats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """
            args = [row.id, row.champion_id,
                    row.hp, row.hp, row.healthregen,
                    row.manaregen, row.armor, row.atkdmg,
                    row.magicresist, row.critdmg, row.movespeed,
                    row.attackrange, row.baseas, row.atkwindup,
                    row.bonusas,
                    row.gameplayradius, row.selectionradius,
                    row.pathingradius, row.acqradius]
            _conn.execute(sql, args)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    Q1Output = open("output/1.out", "w")
    Q1Write = open("output/1.out", "w")

    try:
        sql = """SELECT *
                FROM champion
                GROUP BY champion.id;"""
        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10} {:<15} {:<10} {:<10} {:<10}'.format(
            "id", "name", "price", "lore_id", "championstats_id")
        print(header)
        Q1Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10} {:<15} {:<10} {:<10} {:<10}'.format(
                row[0], row[1], row[2], row[3], row[4])
            print(data)
            Q1Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q1Write.close()
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    Q2Output = open("output/2.out", "w")
    Q2Write = open("output/2.out", "w")

    input = open("input/2.in", "r")
    dataList = input.read().splitlines()

    try:
        sql = """SELECT  championStats.id ,  champion_id ,  hp ,  resource ,  healthregen ,  manaregen ,  armor ,  atkdmg ,  magicresist ,  critdmg ,  movespeed ,  attackrange ,
                baseas ,  atkwindup , bonusas ,  gameplayradius ,  selectionradius ,  pathingradius ,  acqradius
                FROM champion, championStats
                WHERE champion.championstats_id = championStats.id
                AND champion.name = '{}'
                ;""".format(dataList[0])
        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<5} {:<13} {:<13} {:<15} {:<15} {:<12} {:<10} {:<10} {:<10} {:<10} {:<11} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(
            "id", "champion_id", "hp", "resource", "healthregen", "manaregen", "armor", "atkdmg", "magicresist", "critdmg", "movespeed", "attackrange",
            "baseas", "atkwindup", "bonusas", "gameplayradius", "selectionradius", "pathingradius", "acqradius")
        print(header)
        Q2Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<5} {:<13} {:<13} {:<15} {:<15} {:<10} {:<10} {:<10} {:<11} {:<10} {:<11} {:<11} {:<10} {:<10} {:<10} {:<14} {:<15} {:<10} {:<15}'.format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
            print(data)
            Q2Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q2Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    Q3Output = open("output/3.out", "w")
    Q3Write = open("output/3.out", "w")

    input = open("input/3.in", "r")
    dataList = input.read().splitlines()

    try:
        sql = """SELECT  passive, q, w, e, r
                FROM champion, abilityInfo
                WHERE champion.id = abilityInfo.id
                AND champion.name = '{}'
                ;""".format(dataList[0])
        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<50} {:<50} {:<50} {:<50} {:<50}'.format(
            dataList[0] + "'s " + "passive", dataList[0] + "'s " + "q", dataList[0] + "'s " + "w", dataList[0] + "'s " + "e", dataList[0] + "'s " + "r")
        print(header)
        Q3Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<50} {:<50} {:<50} {:<50} {:<50}'.format(
                row[0], row[1], row[2], row[3], row[4])
            print(data)
            Q3Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q3Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    Q4Output = open("output/4.out", "w")
    Q4Write = open("output/4.out", "w")

    input = open("input/4.in", "r")
    dataList = input.read().splitlines()
    print(dataList)

    try:
        sql = """INSERT INTO items VALUES(?,?,?)"""
        args = [dataList[0], dataList[1], dataList[2]]
        args2 = [dataList[3], dataList[4], dataList[5]]
        args3 = [dataList[6], dataList[7], dataList[8]]
        args4 = [dataList[9], dataList[10], dataList[11]]
        args5 = [dataList[12], dataList[13], dataList[14]]

        cursor = _conn.cursor()
        cursor.execute(sql, args)
        cursor.execute(sql, args2)
        cursor.execute(sql, args3)
        cursor.execute(sql, args4)
        cursor.execute(sql, args5)

        header = "This query is just inserting new items into the table"
        Q4Write.write(header + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q4Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    Q5Output = open("output/5.out", "w")
    Q5Write = open("output/5.out", "w")

    #input = open("input/5.in", "r")

    try:  # we are trying to populate champItems table with the new items that we just inserted without making 8 queries
        sql = """SELECT champion.name  
                FROM champion, champRole, role
                WHERE champion.id = champRole.champion_id
                AND role.id = champRole.role_id
                AND role.role_name = "Top"
                AND champion.dmgType = "ad"
            ;"""

        cursor = _conn.cursor()
        cursor.execute(sql)
        # header = '{:<5} {:<15} {:<20}'.format(
        #     "id", "champion_id", "items_id")
        # print(header)
        # Q5Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<5} '.format(
                row[0])
            print(data)

    except Error as e:
        _conn.rollback()
        print(e)

    Q5Write.close()

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populateTables(conn)

        Q1(conn)  # This query is just printing every champion in the database
        Q2(conn)  # This query is printing the champion stats for given champion
        Q3(conn)  # This query is printing the abilityinfo for given champion
        Q4(conn)  # This query is inserting 3 starting items for all champions
        # This query is making the relation between champions and the 3 new items MANY-TO-MANY
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()

# A lot of the code is modified from the code given to us by the professor in Lecture 22 ODBC-Python SQLite.py
# https://datatofish.com/import-csv-sql-server-python/
# A lot of the code is also being taken and modified from Jim's Lab_7.py file from Lab 7
# https://stackoverflow.com/questions/27387415/how-would-i-get-everything-before-a-in-a-string-python/53691831
