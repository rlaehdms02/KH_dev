import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("tips")
df.to_csv("tips")

print(df.isna().sum())

df["tip_pct"] = df["tip"] / df["total_bill"]*100
print(df["tip_pct"])

#단변랑

#이변량

#상관관계

