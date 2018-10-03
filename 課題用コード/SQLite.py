import sqlite3

DATABASE = input("使用するSQLiteのデータベースファイル名を入力してください：")
conn = sqlite3.connect(DATABASE)
while True:
    sql = input("SQL > ")
    if sql == "quit":
        print("終了します")
        break;
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print(f"========")
        if not isinstance(cursor.description,type(None)):
            description = []
            for x in cursor.description:
                description.append(x[0])
            print(f"({','.join(description)})")
        for x in cursor.fetchall():
            print(x)
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    cursor.close()
    conn.commit()
conn.close()
