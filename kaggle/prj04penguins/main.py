import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("penguins")
#종 Gentoo, Chinstrap,Adelie
#섬 Torgersen, Biscoe, Dream
#성별 Female, Male, Nan

#결측치, 중복제거, 인코딩
df = df.dropna().reset_index(drop=True)

#답변량 분석 y
print(df["species"].value_counts())

#x 숫자형 데이터
# fig, axes = plt.subplots(2,2, figsize=(12,8))
# sns.histplot(df["bill_length_mm"], bins=20, ax=axes[0,0])
# axes[0,0].set_title("부리 길이 분포")
# sns.histplot(df["bill_depth_mm"], bins=20, ax=axes[0,1])
# axes[0,1].set_title("부리 깊이 분포")
# sns.histplot(df["flipper_length_mm"], bins=20, ax=axes[1,0])
# axes[1,0].set_title("지느러미 길이")
# sns.histplot(df["body_mass_g"], bins=20, ax=axes[1,1])
# axes[1,1].set_title("체중")
#
# #x 범수형
# fig, axes = plt.subplots(1,3, figsize=(9,4))
# sns.countplot(data = df, x ="species", ax=axes[0])
# axes[0].set_title("종")
# sns.countplot(data = df, x ="island", ax=axes[1])
# axes[1].set_title("섬")
# sns.countplot(data = df, x ="sex", ax=axes[2])
# axes[2].set_title("성별")
# plt.show()

#이변량 분석
#종별로 신체 평균
#print(df.groupby("species")["bill_length_mm"].mean())
#print(df.groupby("species")["bill_depth_mm"].mean())
#print(df.groupby("species")["flipper_length_mm"].mean())
#print(df.groupby("species")["body_mass_g"].mean())
# fig, axes = plt.subplots(2,2,figsize=(12,8))
# sns.boxplot(data=df, ax=axes[0,0], x="species", y="bill_length_mm")
# sns.boxplot(data=df, ax=axes[0,1], x="species", y="bill_depth_mm")
# sns.boxplot(data=df, ax=axes[1,0], x="species", y="flipper_length_mm")
# sns.boxplot(data=df, ax=axes[1,1], x="species", y="body_mass_g")
#
# #종 - 섬, 성별 관계도
# result = pd.crosstab(df["species"], df["island"])
# fig, axes = plt.subplots(1,2,figsize=(6,4))
# sns.heatmap(result, annot=True, ax=axes[0], fmt="d")
# sns.barplot(data=df, ax=axes[1], x="species", y="body_mass_g", hue="sex")

#상관관계
fig, axes = plt.subplots(1,2,figsize=(10,6))
df_nums = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
cor = df_nums.corr()
sns.heatmap(cor, annot=True, ax=axes[0], cmap="coolwarm")

#산점도 : 부리길이, 부리깊이
sns.scatterplot(data=df, x="bill_length_mm", y="flipper_length_mm", hue="species")
plt.tight_layout()
plt.show()




