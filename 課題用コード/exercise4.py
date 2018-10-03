import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

#kmeans方のリファレンス
#http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
def exercise4_1():
    file = 'record.tsv'
    try:
        df = pd.read_table(file)
    except e:
        print('pandas Error occurred:', e.args[0])
        return
    print("=====読み込んだデータ=====")
    print(df)
    df4kmeans = df[['jap','math','eng']] #クラスタリングに用いるデータだけ抜き出す
    k_means = KMeans(init='random', n_clusters=3) #クラスタリングのモデルをつくる
    label = k_means.fit_predict(df4kmeans) #クラスタリングを実行する
    df['label'] = label #クラスタリング結果と元データを対応付ける
    print("=====クラスタリング結果付きデータ=====")
    print(df)
    fig, axes = plt.subplots(nrows=2, ncols=2) #表示領域を作成する
    #以下，クラスタ数に応じて書き換える
    df[df.label == 0].plot.scatter(x='jap', y='math', color='green', ax=axes[0,0])
    df[df.label == 0].plot.scatter(x='math', y='eng', color='green', ax=axes[0,1])
    df[df.label == 0].plot.scatter(x='jap', y='eng', color='green', ax=axes[1,0])
    df[df.label == 1].plot.scatter(x='jap', y='math', color='red', ax=axes[0,0])
    df[df.label == 1].plot.scatter(x='math', y='eng', color='red', ax=axes[0,1])
    df[df.label == 1].plot.scatter(x='jap', y='eng', color='red', ax=axes[1,0])
    df[df.label == 2].plot.scatter(x='jap', y='math', color='blue', ax=axes[0,0])
    df[df.label == 2].plot.scatter(x='math', y='eng', color='blue', ax=axes[0,1])
    df[df.label == 2].plot.scatter(x='jap', y='eng', color='blue', ax=axes[1,0])
    df[df.label == 3].plot.scatter(x='jap', y='math', color='black', ax=axes[0,0])
    df[df.label == 3].plot.scatter(x='math', y='eng', color='black', ax=axes[0,1])
    df[df.label == 3].plot.scatter(x='jap', y='eng', color='black', ax=axes[1,0])
    plt.show()

def exercise4_2():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql('SELECT * FROM info', conn)
    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()
    print("=====読み込んだデータ=====")
    print(df)
    df4kmeans = df[['cnt','temp']] #クラスタリングに用いるデータだけ抜き出す
    k_means = KMeans(init='random', n_clusters=3) #クラスタリングのモデルを作る
    label = k_means.fit_predict(df4kmeans) #クラスタリングを実行する
    df['label'] = label #クラスタリング結果を元データに付与する
    print("=====クラスタリング結果付きデータ=====")
    print(df)
    fig, ax = plt.subplots()
    df[df.label == 0].plot.scatter(x='cnt', y='temp', color='green', ax=ax)
    df[df.label == 1].plot.scatter(x='cnt', y='temp', color='red', ax=ax)
    df[df.label == 2].plot.scatter(x='cnt', y='temp', color='blue', ax=ax)
    #df[df.label == 3].plot.scatter(x='cnt', y='temp', color='black', ax=ax)
    plt.show()

def exercise4_3():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)
    try:
        df = pd.read_sql('SELECT * FROM info', conn)
    except pd.io.sql.DatabaseError as e:
        print('pandas.io.sql.DatabaseError occurred:', e.args[0])
        return
    conn.close()

if __name__=="__main__":
    pd.set_option('display.max_columns', 100) #列方向の省略をなくすための処置
    # exercise4_1()
    exercise4_2()
    #exercise4_3()
