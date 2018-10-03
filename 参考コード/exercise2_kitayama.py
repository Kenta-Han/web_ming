import sqlite3
import csv

# https://crimnut.hateblo.jp/entry/2018/04/17/172709
def showTables(conn):
    cursor = conn.cursor()
    cursor.execute("select tbl_name from sqlite_master where type='table'")
    print("テーブル一覧")
    for x in cursor.fetchall():
        print(x[0])

# https://www.dbonline.jp/sqlite/table/index2.html#section1
def showColumns(conn,table_name):
    cursor = conn.cursor()
    cursor.execute(f"select sql from sqlite_master where type='table' and tbl_name='{table_name}'")
    print(f"{table_name}の定義")
    for x in cursor.fetchall():
        print(x[0])

def showData(conn,table_name,line_num=10):
    cursor = conn.cursor()
    cursor.execute(f"select * from {table_name}")
    print(f"{table_name}の中身")
    description = []
    for x in cursor.description:
        description.append(x[0])
    print(f"({','.join(description)})")
    for x in cursor.fetchall()[:line_num]:
        print(x)

def exercise2_1():
    DATABASE = 'roster.db'
    conn = sqlite3.connect(DATABASE)

    try:
        sql = '''CREATE TABLE person_info
                (student_num TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                gender TEXT CHECK(gender == "male" or gender == "female" or gender == "other"),
                birthday TEXT NOT NULL,
                postcode INTEGER NOT NULL CHECK(postcode < 10000000),
                address TEXT,
                phone_num INTEGER UNIQUE CHECK(phone_num < 10000000000)
                )'''
        conn.execute(sql)
        conn.commit()
        sql = '''CREATE TABLE uni_info
                (student_num TEXT PRIMARY KEY,
                credit INTEGER DEFAULT(148),
                aquisition INTEGER NOT NULL
                )'''
        conn.execute(sql)
        conn.commit()
        showTables(conn)
        showColumns(conn,'person_info')
        showColumns(conn,'uni_info')
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    conn.close()

def exercise2_2():
    DATABASE = 'roster.db'
    conn = sqlite3.connect(DATABASE)

    try:
        #まともパターン
        #sql = '''INSERT INTO person_info VALUES
        #    ("J3-18999","ほげほげ","male","2018/01/01",9999999,"ほげ県",09099999999),
        #    ("J3-18998","ふがふが","female","2018/01/02",8888888,"ふが県",09088888888),
        #    ("J3-18997","ぶーぶー","other","2018/01/03",7777777,"ぶー県",09077777777)
        #    '''
        #まともじゃないパターン（primary）
        sql = '''INSERT INTO person_info VALUES
            ("J3-18999","ほげほげ","male","2018/01/01",1111111,"ほげ県",09022222222)
            '''
        #まともじゃないパターン（not null）
        #sql = '''INSERT INTO person_info VALUES
        #    ("J3-18996",null,"male","2018/01/01",9999999,"ほげ県",09066666666)
        #    '''
        #まともじゃないパターン（check）
        #sql = '''INSERT INTO person_info VALUES
        #    ("J3-18995","もがもが","男","2018/01/01",9999999,"ほげ県",09055555555)
        #    '''
        #まともじゃないパターン（check）
        #sql = '''INSERT INTO person_info VALUES
        #    ("J3-18994","もがもが",null,"2018/01/01",9999999,"ほげ県",09044444444)
        #    '''
        #まともじゃないパターン（check）
        #sql = '''INSERT INTO person_info VALUES
        #    ("J3-18993","もがもが","male","2018/01/01",999999,"ほげ県",09011111111)
        #    '''
        #defaut確認パターン
        sql = '''
            INSERT INTO uni_info VALUES ("J3-18999",null,100)
            '''
        print(sql)
        conn.execute(sql)
        conn.commit()
        showData(conn,'person_info')
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    conn.close()

def exercise2_3():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    try:
        sql = '''CREATE TABLE rental
                (id INTEGER PRIMARY KEY,
                dteday TEXT,
                season INTEGER,
                yr INTEGER,
                mnth INTEGER,
                hr INTEGER,
                holiday INTEGER,
                weekday INTEGER,
                workingday INTEGER,
                weathersit INTEGER,
                temp INTEGER,
                atemp INTEGER,
                hum INTEGER,
                windspeed INTEGER,
                cnt INTEGER
                )'''
        conn.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    try:
        curs = conn.cursor()
        reader = csv.reader(open('train.tsv', 'r'), delimiter= '\t')
        header = next(reader)
        for row in reader:
            #to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
            curs.execute("INSERT INTO rental VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
        conn.commit()
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    showData(conn,'rental')


if __name__=="__main__":
    #exercise2_1()
    #exercise2_2()
    exercise2_3()
