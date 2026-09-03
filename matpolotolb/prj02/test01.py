from logging import info

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#plot 선 marker 점, markersize 크기
#bar 막대기 그래프
#twinx 교차선
#scatter 산점도
#hist 히스토그램
#boxplot 박스플롯
#imshow 이미지 그래프
#violinplot 바이올린
#pie 파이차트
# 0. 데이터 파악해보기
df = pd.read_csv("data/date.csv")
print(df.info())
fig, axes = plt.subplots(2,2, figsize = (10,10))
ax00 = axes[0][0]
ax01 = axes[0][1]
ax10 = axes[1][0]
ax11 = axes[1][1]

# 1. total_bill 히스토그램

plt.subplot(2,2,1)
total = df["total_bill"]
ax00.hist(total)


# 2. 요일별 total_bill 박스플롯
day = df.groupby(["day"])
days = [group["total_bill"].values for name, group in day]
day_labels = [name for name, group in day]
ax01.boxplot(days)

# 3. total_bill 와 tip 산점도 차트
tips = df["tip"]
ax10.scatter(tips, total)

# 4. 요일별 주문 건수 막대그래프




plt.show()