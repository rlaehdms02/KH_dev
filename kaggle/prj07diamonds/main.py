import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
df = sns.load_dataset("diamonds")
df.to_csv("data/diamonds.csv")


# test = ['carat', 'price','x','y','z']
# test01 = df[test].corr()
# cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
# fig, axes = plt.subplots(1,2, figsize=(15,5))
# sns.boxplot(data=df, x = "cut", y = "price", ax = axes[0])
# sns.boxplot(data=df, x = "clarity", y = "price", ax = axes[1])
# plt.show()
# print(test01)


cut_order = ["Fair", 'Good', 'Very Good', 'Premium', 'Ideal']
num_cols = ['carat','depth','table','price','x','y','z']
result = df[num_cols].corr()
print(result)