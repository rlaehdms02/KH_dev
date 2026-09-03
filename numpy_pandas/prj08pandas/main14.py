import pandas as pd

def f01(salary):
    if  salary >= 6000:
        return "고소득자"
    else:
        return "일반"

df = pd.read_csv("data/people.csv")

result = df["연봉"].map(f01)
print(type(result))
print("result : \n", result)