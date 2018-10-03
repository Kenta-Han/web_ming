import sqlite3

dbname = "Record.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# 挿入文
Japanese_insert = ["insert into Japanese(student_num,mark) values('JA01',16),('JA02',88),('JA03',94),('JA04',76),('JA05',41),('JA06',65),('JA07',25),('JA08',68),('JA09',97),('JA10',43)"]
Math_insert = ["insert into Math values('JA01',75),('JA02',60),('JA03',24),('JA04',53),('JA05',49),('JA06',91),('JA07',null),('JA08',62),('JA09',99),('JA10',69)"]
English_insert = ["insert into English values('JA01',54),('JA02',28),('JA03',98),('JA04',71),('JA05',40),('JA06',75),('JA07',66),('JA08',70),('JA09',57),('JA10',47)"]

def create_table_Japanese(conn, c):
	c.execute("create table Japanese(student_num text primary key not null, mark integer)")
	c.execute(Japanese_insert[0])

def create_table_Math(conn, c):
	c.execute("create table Math(student_num text primary key not null, mark integer)");
	c.execute(Math_insert[0])

def create_table_English(conn, c):
	c.execute("create table English(student_num text primary key not null, mark integer)");
	c.execute(English_insert[0])

def getdb(dbname):
	return (conn, c)

def table_isexist_Japanese(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='Japanese'")
	if c.fetchone()[0] == 0:
		return False
	return True

def table_isexist_Math(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='Math'")
	if c.fetchone()[0] == 0:
		return False
	return True

def table_isexist_English(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='English'")
	if c.fetchone()[0] == 0:
		return False
	return True


(conn, c) = getdb(dbname)
if table_isexist_Japanese(conn, c) == False:
	create_table_Japanese(conn, c)
else:
	c.execute(Japanese_insert[0])

if table_isexist_Math(conn, c) == False:
	create_table_Math(conn, c)
else:
	c.execute(Math_insert[0])

if table_isexist_English(conn, c) == False:
	create_table_English(conn, c)
else:
	c.execute(English_insert[0])


conn.commit() # コミット(保存)
conn.close() # 閉じる
