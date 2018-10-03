import sqlite3
import csv

dbname = "rental_bicycle.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()

def create_table_Cycling(conn, c):
	# テーブルを作成
	c.execute("create table info(id integer primary key, dteday text, season integer, yr integer, mnth integer, hr integer, holiday integer, weekday integer, workingday integer, weathersit integer, temp real, atemp real, hum real, windspeed real, cnt integer)")

def getdb(dbname):
	return (conn, c)

def table_isexist_Cycling(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='info'")
	if c.fetchone()[0] == 0:
		return False
	return True

(conn, c) = getdb(dbname)
if table_isexist_Cycling(conn, c) == False:
	create_table_Cycling(conn, c)
else:
	with open('train.tsv', 'r') as f:
		next(f) # 1行目をパス
		reader = csv.reader(f, delimiter= '\t')
		for row in reader:
			to_db = [row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
			c.execute("insert into info(id, dteday, season, yr, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, cnt) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

conn.commit() # コミット(保存)
conn.close() # 閉じる
