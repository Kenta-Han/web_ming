import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
import sqlite3

dbname = "Record.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# データを取り出す
Mark_select = "select * from Mark"

Mark = c.execute(Mark_select).fetchall()

def mark(m):
    all = []
    for i in range(len(m)):
        all.append(m[i][1:])
    return all

# iris データセットをロード
# iris = datasets.load_iris()
# data = iris['data']

data = np.array(mark(Mark))

# kmeans モデルの作成
# クラスタ数は 4 を指定
model = KMeans(n_clusters = 3)
model.fit(data)

# クラスタリング結果ラベルの取得
labels = model.labels_

print(labels)
# 以降，結果の描画
# 1 番目のキャンバスを作成
plt.figure(2)
# ラベル 0 の描画
ldata = data[labels == 0]
print(ldata)
plt.scatter(ldata[:, 0], ldata[:, 1], color='green')
# ラベル 1 の描画
ldata = data[labels == 1]
print(ldata)
plt.scatter(ldata[:, 0], ldata[:, 1], color='red')
# ラベル 2 の描画
ldata = data[labels == 2]
print(ldata)
plt.scatter(ldata[:, 0], ldata[:, 1], color='blue')
# ラベル 3 の描画
ldata = data[labels == 3]
print(ldata)
plt.scatter(ldata[:, 0], ldata[:, 1], color='black')
# x軸、y軸の設定
# plt.xlabel(iris['feature_names'][2])
# plt.ylabel(iris['feature_names'][3])
plt.show()
