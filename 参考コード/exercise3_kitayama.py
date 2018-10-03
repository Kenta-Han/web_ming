import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def showResult(cursor):
    print(f"========")
    if not isinstance(cursor.description,type(None)):
        description = []
        for x in cursor.description:
            description.append(x[0])
        print(f"({','.join(description)})")
    for x in cursor.fetchall():
        print(x)

def exercise3_1():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    sql = 'SELECT sum(cnt),avg(cnt),max(cnt),min(cnt) FROM rental'
    #sql = 'SELECT season,sum(cnt),avg(cnt),max(cnt),min(cnt) FROM rental GROUP BY season'
    #sql = 'SELECT sum(temp),avg(temp),max(temp),min(temp) FROM rental'
    #sql = 'SELECT avg(temp),avg(atemp),avg(temp)-avg(atemp),avg(temp-atemp) FROM rental'
    print(sql)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    showResult(cursor)
    cursor.close()
    conn.commit()
    conn.close()

def exercise3_2():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql('SELECT * FROM rental', conn)
    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()
    print(f"全部：{df.sum()}")
    print(f"合計：{df['cnt'].sum()}")
    print(f"平均：{df['cnt'].mean()}")
    print(f"最大値：{df['cnt'].max()}")
    print(f"最小値：{df['cnt'].min()}")
    print(f"中央値：{df['cnt'].median()}")
    print(f"標準偏差：{df['cnt'].std()}")

    print(f"グループ合計：{df.groupby('season')['cnt'].sum()}")
    print(f"グループ平均：{df.groupby('season')['cnt'].mean()}")
    print(f"グループ最大値：{df.groupby('season')['cnt'].max()}")
    print(f"グループ最小値：{df.groupby('season')['cnt'].min()}")
    print(f"グループ中央値：{df.groupby('season')['cnt'].median()}")
    print(f"グループ標準偏差：{df.groupby('season')['cnt'].std()}")

def exercise3_3():
    plt.style.use('ggplot')
    font = {'family' : 'meiryo'}
    matplotlib.rc('font', **font)

    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql('SELECT * FROM rental', conn)
    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()
    #df.plot.box()
    #df[['temp','atemp']].plot.box()
    #df.plot.scatter(x='hum', y='atemp')
    fig, ax1 = plt.subplots()
    df.groupby('mnth')['temp'].mean().plot(ax=ax1,legend=True)
    ax2 = ax1.twinx()
    df.groupby('mnth')['cnt'].mean().plot.bar(ax=ax2)
    plt.show()

if __name__=="__main__":
    #exercise3_1()
    #exercise3_2()
    exercise3_3()
