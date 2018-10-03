import sqlite3
import csv

def showTables(conn):
    cursor = conn.cursor()
    cursor.execute("select tbl_name from sqlite_master where type='table'")
    print("テーブル一覧")
    for x in cursor.fetchall():
        print(x[0])

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
        sql = "create table person_info(student_num text primary key, name text not null, gender text check(gender = 'male' or gender = 'female' or gender = 'other'), birthday text not null, postcode integer not null check(length(postcode) <= 7), address text, phone_num text unique check(length(phone_num <= 11)))"
        conn.execute(sql)
        conn.commit()
        sql = "create table uni_info(student_num text primary key, credit integer not null default 148, acquisition integer not null)"
        conn.execute(sql)
        conn.commit()
        showTables(conn)
        showColumns(conn,'person_info')
        showColumns(conn,'uni_info')
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    conn.close()

# def exercise2_2():
#     DATABASE = 'roster.db'
#     conn = sqlite3.connect(DATABASE)
#
#     try:
#         Person_insert = ["insert into person_info values('EM-18011', '潘 健太','male','1996/01/31',1320011,'東京都江戸川区','09091366699')"]
# 		conn.execute(Person_insert[0])
#         showData(conn,'person_info')
#
#         Uni_insert = ["insert into uni_info values('EM18011',22,16)"]
# 		conn.execute(Uni_insert[0])
# 		showCloumns(conn,'uni_info')
#     except sqlite3.Error as e:
#         print('sqlite3.Error occurred:', e.args[0])
#     conn.close()

# def exercise2_3():
#     DATABASE = 'rental_bicycle.db'
#     conn = sqlite3.connect(DATABASE)
#
#     try:
#         #ここに，データベースのテーブル定義を書く
#     except sqlite3.Error as e:
#         print('sqlite3.Error occurred:', e.args[0])
#     try:
#         #ここに，train.tsvをインポートするプログラムを書く
#         #基本的にはファイルを読み込んで1行づつデータを挿入していくので良い
#     except sqlite3.Error as e:
#         print('sqlite3.Error occurred:', e.args[0])
#     showData(conn,'#ここにtrain.tsvのデータを入れたテーブル名を書く')

if __name__=="__main__":
    exercise2_1()
    #exercise2_2()
    #exercise2_3()
