import sqlite3

dbname = "roster.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# 挿入文
Person_insert = ["insert into person_info values('EM-18011', '潘 健太','male','1996/01/31','1320011','東京都江戸川区','09091366699')"]
Uni_insert = ["insert into uni_info values('EM18011',22,16)"]

# エラーを試す
# Person_insert = ["insert into Person_info values('EM-18012', '潘 健太','male','1996/01/31','1320011','東京都江戸川区','09091366699')"]
# Uni_insert = ["insert into Uni_info(student_num,acquisition) values('EM18012',16)"]

def create_table_Person(conn, c):
    # テーブルを作成
	c.execute("create table person_info(student_num text primary key, name text not null, gender text check(gender = 'male' or gender = 'female' or gender = 'other'), birthday text not null, postcode text not null check(length(postcode) <= 7), address text, phone_num text unique check(length(phone_num <= 11)))")
	c.execute(Person_insert[0])

def create_table_Uni(conn, c):
	c.execute("create table uni_info(student_num text primary key, credit integer not null default 148, acquisition integer not null)");
	c.execute(Uni_insert[0])

def getdb(dbname):
	return (conn, c)

def table_isexist_Person(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='Person_info'")
	if c.fetchone()[0] == 0:
		return False
	return True

def table_isexist_Uni(conn, c):
	c.execute("select count(*) from sqlite_master where type='table' and name='Uni_info'")
	if c.fetchone()[0] == 0:
		return False
	return True

(conn, c) = getdb(dbname)
if table_isexist_Person(conn, c) == False:
	create_table_Person(conn, c)
else:
	c.execute(Person_insert[0])

if table_isexist_Uni(conn, c) == False:
	create_table_Uni(conn, c)
else:
	c.execute(Uni_insert[0])

conn.commit() # コミット(保存)
conn.close() # 閉じる
