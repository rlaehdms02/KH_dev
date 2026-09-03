import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("tips")
df.to_csv("data/tips.csv")

num_cols = ['total_bill','tip']
x = df[num_cols].corr()
print(x)