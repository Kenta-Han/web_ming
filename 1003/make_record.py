import sqlite3
import csv

dbname = "Record.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# 挿入文
# Mark_insert = ["insert into Mark(student_num,jap,math,eng) values('JA01',16,100,54),('JA02',88,60,78),('JA03',94,24,98),('JA04',76,53,71),('JA05',41,49,40),('JA06',85,91,35),('JA07',25,81,86),('JA08',68,62,70),('JA09',97,99,92),('JA10',73,69,47)"]

def create_table_Mark(conn, c):
	c.execute("create table Mark(student_num text primary key not null, jap integer,math integer,eng integer)")
	# c.execute(Mark_insert[0])
	openfile()

def getdb(dbname):
	return (conn, c)

def table_isexist_Mark(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='Mark'")
	if c.fetchone()[0] == 0:
		return False
	return True

def openfile():
	with open('record.csv', 'r') as f:
		next(f) # 1行目をパス
		reader = csv.reader(f, delimiter= '\t')
		for row in reader:
			to_db = [row[0], row[1],row[2],row[3]]
			c.execute("insert into Mark(student_num, jap, math, eng) values(?, ?, ?, ?);", to_db)

(conn, c) = getdb(dbname)
if table_isexist_Mark(conn, c) == False:
	create_table_Mark(conn, c)
else:
	openfile()

conn.commit() # コミット(保存)
conn.close() # 閉じる
