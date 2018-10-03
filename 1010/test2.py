import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from pandas.tools import plotting # 高度なプロットを行うツールのインポート

def exercise5_1():
    DATABASE = 'rental_bicycle.db'
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    df = pd.read_sql('SELECT * FROM info', conn)
    # print(df.head()) #データの確認
    # 10~14列のデータを使う(温度(temp)，体感温度(atemp)，湿度(hum)，風速(windspeed)を使って),100行まで
    # print(df.iloc[:,10:14].head())

    # 全体像を眺める
    # plotting.scatter_matrix(df[df.columns[10:14]], figsize=(6,6), alpha=0.8, diagonal='kde')
    # plt.show()

    from scipy.cluster.hierarchy import linkage, dendrogram
    result = linkage(df.iloc[:100, 10:14], metric = 'braycurtis',method = 'average')

    dendrogram(result)
    plt.title("Title")
    plt.ylabel("points")
    plt.show()

if __name__=="__main__":
    exercise5_1()
