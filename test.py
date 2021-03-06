import sklearn
from sklearn.datasets import load_boston
from sklearn import linear_model
import pandas as pd
import numpy as np


from pandas import Series,DataFrame

import matplotlib.pyplot as plt
#データを取得（ボストン住宅価格）
boston = load_boston()
#データフレームに格納
boston_df = DataFrame(boston.data)
#カラムを設定
boston_df.columns = boston.feature_names
#カラムを追加
boston_df["PRICE"] = DataFrame(boston.target)

#*********重回帰分析***********

#インスタンス
#linear_regression = linear_regression()

x = boston_df.drop("PRICE",1)

y = boston_df.PRICE


clf = linear_model.LinearRegression()

clf.fit(x,y)
print("切片：",clf.intercept_)
print("回帰係数：",clf.coef_)
print("決定係数：",clf.score(x,y))
#print(boston_df)
plt.scatter(boston_df["PRICE"],boston_df["CRIM"])
plt.show()
