import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#설정 안하면 1,1
fig, ax =plt.subplots(figsize=(10,5))

fig.suptitle("오늘은 금요일")

x = np.linspace(0,10,10)
y1 = x
y2 = x ** 1.5
y3 = x ** 2

#plot 선그래프, marker 점 표시, markersize 점 크기
ax.plot(x, y1, marker="o", markersize=10, linestyle="-", color="red", linewidth=2, label = "레모네이드판매량")
ax.plot(x, y2, marker="s", markersize=10, linestyle="--", color="blue", linewidth=3, label = "기온")
ax.plot(x, y3, marker="^", markersize=10, linestyle=":", color="green", linewidth=4, label = "강수량")

ax.set_xlabel("x축라벨")
ax.set_ylabel("y축라벨")
ax.set_title("현재 그래프 제목")

ax.legend()
#savefig 이미지 파일로 저장
#plt.savefig("test.svg")

#show 그래프 표시
plt.show()

