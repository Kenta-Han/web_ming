import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def exercise3_1():
    dbname = "rental_bicycle.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 利用者数の総和、平均、MAX、MIN
    sql = 'select sum(cnt),avg(cnt),max(cnt),min(cnt) from info'
    cur.execute(sql)
    data = cur.fetchall()[0]
    print('利用者数\t総和：{sum}, 平均：{ave}, 最大：{max}, 最小：{min}'.format(sum = data[0], ave = data[1], max = data[2], min = data[3]))

    # 季節ごとの利用者数の総和、平均、MAX、MIN
    sea = {1:'春',2:'夏',3:'秋',4:'冬'}
    sql = 'select season,sum(cnt),avg(cnt),max(cnt),min(cnt) from info group by season order by season ASC'
    cur.execute(sql)
    print('季節別利用者データ')
    for data in cur.fetchall():
        print('{season}\t総和：{sum}, 平均：{ave}, 最大：{max}, 最小：{min}'.format(season = sea[data[0]], sum = data[1], ave = data[2], max = data[3], min = data[4]))

    # 年間気温の総和、平均、MAX、MIN
    yea = {0:'2011',1:'2012'}
    sql = 'select yr,sum(temp),avg(temp),max(temp),min(temp) from info group by yr order by yr ASC'
    cur.execute(sql)
    print('年間別利用者データ')
    for data in cur.fetchall():
        print('{year}\t総和：{sum}, 平均：{ave}, 最大：{max}, 最小：{min}'.format(year = yea[data[0]], sum = data[1], ave = data[2], max = data[3], min = data[4]))

    # 温度と体感温度の平均の差
    sql = 'select (avg(temp)*(39+8)-8)-(avg(atemp)*(50+16)-16) from info'
    cur.execute(sql)
    data = cur.fetchall()
    print('温度と体感温度の平均の差\t{sa}'.format(sa = data))
    conn.close()

def exercise3_2():
    dbname = "rental_bicycle.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 利用者数の総和，平均，標準偏差，中央値，最大値，最小値
    cnt_select = "select cnt from info"
    cnt = [i[0] for i in cur.execute(cnt_select).fetchall()]
    print("総和:{sum}".format(sum = np.sum(cnt)))
    print("平均:{ave}".format(ave = np.average(cnt)))
    print("標準偏差:{std}".format(std = np.std(cnt)))
    print("中央値:{median}".format(median = np.median(cnt)))
    print("最大値:{max}".format(max = max(cnt)))
    print("最小値:{min}".format(min = min(cnt)))

    # 季節毎の利用者数の平均，中央値，最大値，最小値
    conn.close()

def exercise3_3():
    dbname = "rental_bicycle.db"
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # 温度と体感温度に関する箱ひげ図を作成せよ
    t_max, t_min = 39.0, -8.0
    rev = t_max - t_min
    at_max, at_min = 50.0, -16.0
    a_rev = at_max - at_min

    sql = 'SELECT temp * ({rev}) + {t_min}, atemp * ({a_rev}) + {at_min} FROM info'.format(rev = rev,t_min = t_min, a_rev = a_rev, at_min = at_min)
    cur.execute(sql)
    temp_list, atemp_list = [], []
    for data in cur.fetchall():
        temp_list.append(data[0])
        atemp_list.append(data[1])

    points = (temp_list,atemp_list)
    fig, ax = plt.subplots()
    bp = ax.boxplot(points)
    ax.set_xticklabels(['temp', 'atemp'])
    plt.title('temp & atemp')
    plt.xlabel('name')
    plt.ylabel('points')
    # Y軸のメモリのrange
    plt.ylim([-20,55])
    plt.grid()
    plt.show()

    # 湿度と体感温度を使って散布図を作成
    sql = "select hum, atemp * ({a_rev}) + {at_min} from info".format(a_rev = a_rev,at_min = at_min)
    cur.execute(sql)
    hum_list, atemp_list = [], []
    for data in cur.fetchall():
        hum_list.append(data[0])
        atemp_list.append(data[1])

    plt.scatter(hum_list, atemp_list,s=10, c="yellow", marker="*", alpha=0.5,linewidths="2", edgecolors="orange")
    plt.title("title")
    plt.xlabel('hum')
    plt.ylabel('atemp')
    plt.grid(True)
    plt.show()

    # 月ごとの利用者数の平均を棒グラフで表し，同じ図に月ごとの平均気温を折れ線グラフで表せ
    sql = "select mnth, avg(cnt), avg(temp) * ({rev}) + {t_min} from info group by mnth order by mnth".format(rev = rev,t_min = t_min)
    cur.execute(sql)
    mnth = np.array([i for i in range(12)])
    cnt_list, temp_list = [], []
    for data in cur.fetchall():
        cnt_list.append(data[1])
        temp_list.append(data[2])

    cnt_list, temp_list = np.array(cnt_list), np.array(temp_list)
    # 棒グラフを出力
    fig, ax1 = plt.subplots()
    ax1.bar(mnth, cnt_list, align="center", color="royalblue", linewidth=0)
    ax1.set_ylabel('Month Average Cnt')

    # 折れ線グラフを出力
    ax2 = ax1.twinx()
    ax2.plot(mnth, temp_list, linewidth=4, color="crimson",marker="*",markersize=10)
    ax2.set_ylabel('Month Average Temp')
    plt.show()

    conn.close()

if __name__=="__main__":
    # exercise3_1()
    # exercise3_2()
    exercise3_3()
