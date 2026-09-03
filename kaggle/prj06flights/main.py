import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("flights")
df.to_csv("data/flights.csv")

x =df["year"].astype(str) +  "-" +df["month"].astype(str)
df["date"] = pd.to_datetime(x, format="%Y-%b")
df.sort_values("date").reset_index(drop=True)
print(df)

# plt.figure(figsize = (15,5))
# plt.plot(df["date"], df["passengers"])
# plt.show()

plt.figure(figsize = (15,5))
sns.barplot(data = df, x="month", y="passengers")
plt.show()