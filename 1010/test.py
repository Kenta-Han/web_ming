import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris

# iris データセットの読み込み
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_labels = list(map(lambda t: iris.target_names[t], iris.target))

# 階層型クラスタリングの実施
# ウォード法 x ユークリッド距離
linkage_result = linkage(iris_df, method='ward', metric='euclidean')

# クラスタ分けするしきい値を決める
threshold = 0.7 * np.max(linkage_result[:, 2])

# 階層型クラスタリングの可視化
plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k')
dendrogram(linkage_result, labels=iris_labels, color_threshold=threshold)
plt.show()

# クラスタリング結果の値を取得
clustered = fcluster(linkage_result, threshold, criterion='distance')

# クラスタリング結果を比較
print(clustered)
print(iris.target)
