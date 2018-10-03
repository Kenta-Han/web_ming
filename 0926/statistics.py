import sqlite3
import matplotlib.pyplot as plt
import numpy as np

dbname = "Record.sqlite3"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# データを取り出す
Japanese_select = "select * from Japanese"
Math_select = "select * from Math"
English_select = "select * from English"

Japanese = c.execute(Japanese_select).fetchall()
Math = c.execute(Math_select).fetchall()
English = c.execute(English_select).fetchall()

def ave(subject):
    sum = 0
    cnt = 0
    for i in range(len(subject)):
        everyone = subject[i][1]
        if isinstance(everyone, int) == True:
            sum = sum + everyone
            cnt += 1
    return sum/cnt

# 平均
print("Japanese;" + str(ave(Japanese)))
print("Math:" + str(ave(Math)))
print("English:" + str(ave(English)))

def mark(subject):
    all = []
    for i in range(len(subject)):
        all.append(subject[i][1])
    return all

print(mark(Japanese))
print(mark(English))

# 点数のタプル
points = (mark(Japanese), mark(English))

print(points)
# 箱ひげ図
fig, ax = plt.subplots()

bp = ax.boxplot(points)
ax.set_xticklabels(['Japanese', 'English'])

plt.title('Box plot')
plt.xlabel('exams')
plt.ylabel('point')
# Y軸のメモリのrange
plt.ylim([0,100])
plt.grid()

# 描画
plt.show()

conn.close() # 閉じる
