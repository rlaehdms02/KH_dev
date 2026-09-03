import pandas as pd

df = pd.read_csv("data/people.csv")

#print(df[(df["나이"] < 40) | (df["나이"] >=30)])

# print(df[(df["도시"].isin(["서울", "부산"]))])
#print(df[df["나이"].isin("나이" >=30 | "나이" < 40)])
mask2 = df["나이"] >=30
mask1 = df["나이"] <40
mask = df["나이"].between(30, 39)
print(df[mask])