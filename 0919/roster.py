import sqlite3

dbname = "roster.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# 挿入文
Person_insert = ["insert into Person_info values('EM-18011', '潘 健太',1,'1996/01/31','132-0011','東京都江戸川区','09091366699')"]
Uni_insert = ["insert into Uni_info values('EM18011',22,16)"]

def create_table_Person(conn, c):
    # テーブルを作成
	c.execute("create table Person_info(student_num text primary key not null, name text not null, gender integer not null, birthday text not null, postcode integer not null, address text, phone_num text)")
	c.execute(Person_insert[0])

def create_table_Uni(conn, c):
	c.execute("create table Uni_info(student_num text primary key not null, credit integer not null, acquisition integer not null)");
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