import sqlite3
import matplotlib.pyplot as plt
import numpy as np

dbname = "Record.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# データを取り出す
Japanese_select = "select mark from Japanese"
Math_select = "select mark from Math"
English_select = "select mark from English"

Japanese = c.execute(Japanese_select).fetchall()
Math = c.execute(Math_select).fetchall()
English = c.execute(English_select).fetchall()


# 総和
print("=== sum ===")
print("Japanese:" + str(np.sum(Japanese)))
# print("Math:" + str(np.sum(Math)))
print("English:" + str(np.sum(English)))
# 平均
print("=== average ===")
print("Japanese:" + str(np.average(Japanese)))
# print("Math:" + str(np.average(Math)))
print("English:" + str(np.average(English)))
# 分散
print("=== var ===")
print("Japanese:" + str(np.var(Japanese)))
print("English:" + str(np.var(English)))


def mark(subject):
    all = []
    for i in range(len(subject)):
        all.append(subject[i][0])
    return all

# 点数のタプル
points = (mark(Japanese),mark(English))
# 箱ひげ図
fig, ax = plt.subplots()

bp = ax.boxplot(points)
# データ名
ax.set_xticklabels(['Japanese', 'English'])

plt.title('Japanese & English Box Plot')
# ラベル名
plt.xlabel('subject')
plt.ylabel('points')
# Y軸のメモリの長さ
plt.ylim([0,100])
plt.grid()

# 描画
plt.show()

conn.close() # 閉じる
