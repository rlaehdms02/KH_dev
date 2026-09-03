import seaborn as sns

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("tips")

fig, ax = plt.subplots(2,3,figsize=(12,8))

#hisplot
sns.histplot(df["total_bill"], bins=20 , kde=True ,ax=ax[0,0])

#boxplot
sns.boxplot( data=df, x="day", y="total_bill", ax=ax[0,1])

#scatterplot
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day",ax = ax[1,0])

#heatmap
c = df[["total_bill", "tip","size"]].corr()
sns.heatmap(data=c, annot=True ,ax=ax[1,1])

#countplot
sns.countplot(data = df, ax=ax[0,2], x = "day", hue="sex")
#pairplot
result = sns.pairplot(data = df)
result.savefig("result.svg")

plt.show()
