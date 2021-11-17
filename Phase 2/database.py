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

        sql = """CREATE TABLE users (
                    id INTEGER NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    username VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    types INTEGER NOT NULL)"""  # GOOD
        _conn.execute(sql)

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

        sql = "DROP TABLE championSkins"
        _conn.execute(sql)

        sql = "DROP TABLE championStats"
        _conn.execute(sql)

        sql = "DROP TABLE users"
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

        users = pandas.read_csv(r'data/users.csv')
        usersdf = pandas.DataFrame(users)
        for row in usersdf.itertuples():

            sql = """INSERT INTO users VALUES(?,?,?,?,?)
                    """
            args = [row.id, row.name, row.username, row.password, row.types]
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

    try:
        sql = """INSERT INTO items VALUES(?,?,?)"""
        args = [dataList[0], dataList[1], dataList[2]]
        args2 = [dataList[3], dataList[4], dataList[5]]
        args3 = [dataList[6], dataList[7], dataList[8]]
        args4 = [dataList[9], dataList[10], dataList[11]]
        args5 = [dataList[12], dataList[13], dataList[14]]
        args6 = [dataList[15], dataList[16], dataList[17]]
        args7 = [dataList[18], dataList[19], dataList[20]]
        args8 = [dataList[21], dataList[22], dataList[23]]
        args9 = [dataList[24], dataList[25], dataList[26]]
        args10 = [dataList[27], dataList[28], dataList[29]]
        args11 = [dataList[30], dataList[31], dataList[32]]
        args12 = [dataList[33], dataList[34], dataList[35]]

        cursor = _conn.cursor()
        cursor.execute(sql, args)
        cursor.execute(sql, args2)
        cursor.execute(sql, args3)
        cursor.execute(sql, args4)
        cursor.execute(sql, args5)
        cursor.execute(sql, args6)
        cursor.execute(sql, args7)
        cursor.execute(sql, args8)
        cursor.execute(sql, args9)
        cursor.execute(sql, args10)
        cursor.execute(sql, args11)
        cursor.execute(sql, args12)

        header = "This query is just inserting new items into the table"
        Q4Write.write(header + '\n')
        _conn.commit()
        print("success")

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

    input = open("input/5.in", "r")
    dataList = input.read().splitlines()

    try:
        sql = """INSERT INTO champItems VALUES(?,?,?)"""
        args = [dataList[0], dataList[1], dataList[2]]
        args2 = [dataList[3], dataList[4], dataList[5]]
        args3 = [dataList[6], dataList[7], dataList[8]]
        args4 = [dataList[9], dataList[10], dataList[11]]
        args5 = [dataList[12], dataList[13], dataList[14]]
        args6 = [dataList[15], dataList[16], dataList[17]]
        args7 = [dataList[18], dataList[19], dataList[20]]
        args8 = [dataList[21], dataList[22], dataList[23]]
        args9 = [dataList[24], dataList[25], dataList[26]]
        args10 = [dataList[27], dataList[28], dataList[29]]
        args11 = [dataList[30], dataList[31], dataList[32]]
        args12 = [dataList[33], dataList[34], dataList[35]]
        args13 = [dataList[36], dataList[37], dataList[38]]
        args14 = [dataList[39], dataList[40], dataList[41]]
        args15 = [dataList[42], dataList[43], dataList[44]]

        cursor = _conn.cursor()
        cursor.execute(sql, args)
        cursor.execute(sql, args2)
        cursor.execute(sql, args3)
        cursor.execute(sql, args4)
        cursor.execute(sql, args5)
        cursor.execute(sql, args6)
        cursor.execute(sql, args8)
        cursor.execute(sql, args9)
        cursor.execute(sql, args10)
        cursor.execute(sql, args11)
        cursor.execute(sql, args12)
        cursor.execute(sql, args13)
        cursor.execute(sql, args14)
        cursor.execute(sql, args15)

        header = "This query is just inserting champion and their items into the table"
        Q5Write.write(header + '\n')
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    Q5Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    Q6Output = open("output/6.out", "w")
    Q6Write = open("output/6.out", "w")

    try:  # modifying the existing movespeed of ad champs by multiplying itself by 2
        sql = """UPDATE championStats SET movespeed = movespeed * 2
                WHERE championStats.champion_id IN(SELECT championStats.champion_id FROM championStats, champion WHERE championStats.champion_id = champion.id AND champion.dmgType = 'ad')
            ;"""

        cursor = _conn.cursor()
        cursor.execute(sql)

        header = "This query is just modifying movespeed if champion dmgType is ad"
        Q6Write.write(header + '\n')
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    Q6Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    Q7Output = open("output/7.out", "w")
    Q7Write = open("output/7.out", "w")

    try:  # This query is just printing AD champion items
        sql = """SELECT items.name
                FROM champion, champItems, items
                WHERE champion.id = champItems.champion_id
                AND items.id = champItems.items_id
                AND champion.dmgType = 'ad'
                GROUP BY items.name
            ;"""

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10}'.format(
            'Items')
        print(header)
        Q7Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10}'.format(
                row[0])
            print(data)
            Q7Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q7Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")

    Q8Output = open("output/8.out", "w")
    Q8Write = open("output/8.out", "w")

    input = open("input/8.in", "r")
    dataList = input.read().splitlines()
    # Printing skins for given champion
    try:
        sql = """ SELECT championSkins.name
                FROM champion, championSkins
                WHERE champion.id = championSkins.champion_id
                AND champion.name = '{}';""".format(dataList[0])

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10}'.format(
            dataList[0] + ' Skins')
        print(header)
        Q8Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10}'.format(
                row[0])
            print(data)
            Q8Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q8Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    Q9Output = open("output/9.out", "w")
    Q9Write = open("output/9.out", "w")

    input = open("input/9.in", "r")
    dataList = input.read().splitlines()

    # Printing champions in mid lane
    try:
        sql = """ SELECT champion.name
                FROM champion, role, champRole
                WHERE champion.id = champRole.champion_id
                AND role.id = champRole.role_id
                AND role.role_name = "{}"
                """.format(dataList[0])

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10}'.format(
            "Champion")
        print(header)
        Q9Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10}'.format(
                row[0])
            print(data)
            Q9Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q9Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    Q10Output = open("output/10.out", "w")
    Q10Write = open("output/10.out", "w")

    # Printing champions in mid lane
    try:
        sql = """ DELETE FROM championSkins
                WHERE championskins.name like "%High Noon%";
                """

        cursor = _conn.cursor()
        cursor.execute(sql)

        print("this query is deleting skins with the name High Noon")
        Q10Write.write(
            "this query is deleting skins with the name High Noon" + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q10Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    Q11Output = open("output/11.out", "w")
    Q11Write = open("output/11.out", "w")

    # Print all champions with highest price
    try:
        sql = """SELECT name, price
                FROM champion
                WHERE price == (SELECT MAX(price) FROM champion)
                ORDER BY price DESC, name;
                """

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10} {:<10}'.format(
            "Champion", "Price")
        print(header)
        Q11Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10} {:<10}'.format(
                row[0], row[1])
            print(data)
            Q11Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q11Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    Q12Output = open("output/12.out", "w")
    Q12Write = open("output/12.out", "w")

    # Reduce price of all tank items
    try:
        sql = """UPDATE items SET price = price - 400
                WHERE items.name IN(SELECT items.name
                FROM champion, items, champItems
                WHERE champion.id = champItems.champion_id
                AND items.id = champItems.items_id
                AND champion.dmgType = "tank"
                GROUP BY items.name);
                """

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = "This query is reducing the price of all tank items by 400"
        print(header)
        Q12Write.write(
            header + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q12Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    Q13Output = open("output/13.out", "w")
    Q13Write = open("output/13.out", "w")

    # gets a list of all admin users
    try:
        sql = """SELECT users.username
                FROM users
                WHERe users.types = 1;
                """

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10}'.format(
            "Admin Users username")
        print(header)
        Q13Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10}'.format(
                row[0])
            print(data)
            Q13Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q13Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    Q14Output = open("output/14.out", "w")
    Q14Write = open("output/14.out", "w")

    try:
        sql = """SELECT * FROM users
                WHERE users.password IN(
                    SELECT users.password
                    FROM users
                    GROUP BY users.password
                    HAVING COUNT(*) > 1
                );
                """

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10} {:<10}'.format(
            "ID", "Name")
        print(header)
        Q14Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10} {:<10}'.format(
                row[0], row[1])
            print(data)
            Q14Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q14Write.close()

    print("++++++++++++++++++++++++++++++++++")

# SELECT CAST(championStats.hp as INT) converts string to integer until '-'
# SUBSTR(championStats.hp, 7, 10) grabs max hp
# SUBSTR(championStats.hp, 1, 4) grabs min hp
# CAST(SUBSTR(championStats.hp, 1, 4) AS INT) converts string into integer


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    Q15Output = open("output/15.out", "w")
    Q15Write = open("output/15.out", "w")

    try:
        sql = """
        SELECT champion.name, MAX(CAST(SUBSTR(championStats.hp, 7,10) AS INT)) 
        FROM championStats, champion
        WHERE champion.id = championStats.champion_id;"""

        cursor = _conn.cursor()
        cursor.execute(sql)
        header = '{:<10} {:<10}'.format(
            "Champion", "Base Max Hp")
        print(header)
        Q15Write.write(header + '\n')
        rows = cursor.fetchall()
        for row in rows:
            # print(row)
            data = '{:<10} {:<10}'.format(
                row[0], row[1])
            print(data)
            Q15Write.write(data + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    Q15Write.close()

    print("++++++++++++++++++++++++++++++++++")


def Q16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q16")

    Q16Output = open("output/16.out", "w")
    Q16Write = open("output/16.out", "w")

    try:
        input = pandas.read_csv(r'input/teemo.csv')
        inputdf = pandas.DataFrame(input)
        for row in inputdf.itertuples():
            sql = """INSERT INTO champion VALUES(?,?,?,?,?,?,?)
                    """
            args = [row.id, row.name, row.price, row.lore_id,
                    row.championstats_id, row.abilityinfo_id, row.dmgType]
            _conn.execute(sql, args)

            sql = """INSERT INTO championStats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """
            args = [row.id, row.id, row.hp, row.resource, row.healthregen, row. manaregen,
                    row.armor, row.atkdmg, row.magicresist, row.critdmg, row.movespeed,
                    row.attackrange, row.baseas, row.atkwindup, row.bonusas, row.gameplayradius,
                    row.selectionradius, row.pathingradius, row.acqradius]
            _conn.execute(sql, args)

            sql = """INSERT INTO champItems VALUES(?,?,?)
                    """
            args = [36, row.id, row.items_id1]
            _conn.execute(sql, args)

            sql = """INSERT INTO champItems VALUES(?,?,?)
                    """
            args = [37, row.id, row.items_id2]
            _conn.execute(sql, args)

            sql = """INSERT INTO champItems VALUES(?,?,?)
                    """
            args = [38, row.id, row.items_id3]
            _conn.execute(sql, args)

            sql = """INSERT INTO champItems VALUES(?,?,?)
                    """
            args = [39, row.id, row.items_id4]
            _conn.execute(sql, args)

            sql = """INSERT INTO lore VALUES(?,?,?)
                    """
            args = [row.id, row.id, row.lore_description]
            _conn.execute(sql, args)

            sql = """INSERT INTO champRole VALUES(?,?,?)
                    """
            args = [22, row.id, row.role_id]
            _conn.execute(sql, args)

            sql = """INSERT INTO abilityInfo VALUES(?,?,?,?,?,?,?)
                    """
            args = [row.id, row.id, row.passive, row.q, row.w,
                    row.e, row.r]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [147, row.id, row.skin1name, row.skin1price, row.skin1chroma,
                    row.skin1prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [148, row.id, row.skin2name, row.skin2price, row.skin2chroma,
                    row.skin2prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [149, row.id, row.skin3name, row.skin3price, row.skin3chroma,
                    row.skin3prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [150, row.id, row.skin4name, row.skin4price, row.skin4chroma,
                    row.skin4prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [151, row.id, row.skin5name, row.skin5price, row.skin5chroma,
                    row.skin5prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [152, row.id, row.skin6name, row.skin6price, row.skin6chroma,
                    row.skin6prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [153, row.id, row.skin7name, row.skin7price, row.skin7chroma,
                    row.skin7prestige_edition]
            _conn.execute(sql, args)

            sql = """INSERT INTO championSkins VALUES(?,?,?,?,?,?)
                    """
            args = [154, row.id, row.skin8name, row.skin8price, row.skin8chroma,
                    row.skin8prestige_edition]
            _conn.execute(sql, args)

        header = "This query is just inserting Teemo"
        Q16Write.write(header + '\n')
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    Q16Write.close()

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
        Q5(conn)  # This query is inserting the champ and items relationship
        Q6(conn)  # This query is modifying movespeed *2 for any ad champ
        Q7(conn)  # This query is just printing AD champion items
        Q8(conn)  # This query will print skins for champion
        Q9(conn)  # This query will print champions that go in mid lane
        Q10(conn)  # This query will delete chapmions with the Highnoon skin line
        Q11(conn)  # This query will print champions from with the highest cost
        Q12(conn)  # This query will modify all tank items, reducing price by 400
        Q13(conn)  # This query will list find all admins
        Q14(conn)  # This query will find all users with last name Jones
        Q15(conn)  # This query will find the max health from champions
        Q16(conn)  # This query will add teemo
    closeConnection(conn, database)


if __name__ == '__main__':
    main()

# A lot of the code is modified from the code given to us by the professor in Lecture 22 ODBC-Python SQLite.py
# https://datatofish.com/import-csv-sql-server-python/
# A lot of the code is also being taken and modified from Jim's Lab_7.py file from Lab 7
# https://stackoverflow.com/questions/27387415/how-would-i-get-everything-before-a-in-a-string-python/53691831
