import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np


df = pd.read_excel("onogami.xlsx")
x = df.loc[:,["安値"]]
y = df.loc[:,["終値"]]
clf = linear_model.LinearRegression()

#シリーズ型だとエラーが出る
clf.fit(x,y)
print(clf.coef_[0][0])
plt.scatter(x,y)
plt.show()