import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("diamonds")
df.to_csv("diamonds.csv")

#전처리

df = df[(df["x"] > 0) & (df["y"] > 0) & (df["z"] > 0)]

# fig, axes = plt.subplots(1,2,figsize = (10,8))
# sns.histplot(data = df["price"] ,ax =axes[0], bins = 10)
# sns.histplot(data = df["carat"], ax =axes[1])
# plt.show()

#이변량
#alpha는 점 투명도
# fig, axes = plt.subplots(1,3,figsize = (15,5))
# sns.scatterplot(data = df, x = df["carat"], y=df["price"] , ax = axes[0], alpha=0.1)
# sns.scatterplot(data = df, x = df["color"], y=df["price"] , ax = axes[1], alpha=0.1)
# sns.scatterplot(data = df, x = df["depth"], y=df["price"] , ax = axes[2], alpha=0.1)
# plt.show()

#상관관계수
test = ['carat','depth','table','price','x','y','z']
result = df[test].corr()
print(result)

#인사이트
