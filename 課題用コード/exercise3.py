import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

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
    cur = conn.cursor()

    # sql = 'ここに利用者数の総和，平均，最大値，最小値を出すSQL文を書こう'
    sql = 'select sum(cnt),avg(cnt),max(cnt),min(cnt) from info'
    #sql = 'ここに季節毎の利用者数の総和，平均，最大値，最小値を出すSQL文を書こう'
    #sql = 'ここに年間温度の平均，最大値，最小値を出すSQL文を書こう'
    #sql = 'ここに温度と体感温度の平均の差を出すSQL文を書こう'

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
        df = pd.read_sql('SELECT * FROM info', conn)
        print("\n==利用者数の総和，平均，標準偏差，中央値，最大値，最小値==")
        print("総和:{sum}".format(sum = df['cnt'].sum()))
        print("平均:{ave}".format(ave = df['cnt'].mean()))
        print("標準偏差:{std}".format(std = df['cnt'].std()))
        print("中央値:{median}".format(median = df['cnt'].median()))
        print("最大値:{max}".format(max = max(df['cnt'])))
        print("最小値:{min}".format(min = min(df['cnt'])))

        print("\n==季節毎の利用者数の総和，平均，標準偏差，中央値，最大値，最小値==")
        print("総和:{sum}".format(sum = df[df.season==1]['cnt'].sum()))
        print("平均:{ave}".format(ave = df[df.season==1]['cnt'].mean()))
        print("標準偏差:{std}".format(std = df[df.season==1]['cnt'].std()))
        print("中央値:{median}".format(median = df[df.season==1]['cnt'].median()))
        print("最大値:{max}".format(max = max(df[df.season==1]['cnt'])))
        print("最小値:{min}".format(min = min(df[df.season==1]['cnt'])))

    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()
    '''
        dfにpandasのデータフレーム型として，SELECT * FROM rental の結果が入っている．
        データフレームを操作して，課題をこなそう．
    '''

def exercise3_3():
    #表示のためのおまじない．意味は調べよう．
    plt.style.use('ggplot')
    font = {'family' : 'meiryo'}
    matplotlib.rc('font', **font)

    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql('SELECT * FROM info', conn)
    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()
    '''
        ここに各種図を表示するプログラムを書こう．
    '''

if __name__=="__main__":
    exercise3_1()
    exercise3_2()
    exercise3_3()
