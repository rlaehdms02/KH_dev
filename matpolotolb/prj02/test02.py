import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(6, 6))

month   = ["1월", "2월", "3월", "4월", "5월", "6월"]
gangnam = [120, 135, 128, 150, 175, 210]   # 강남점
hongdae = [95, 110, 130, 125, 160, 185]    # 홍대점


plt.ylim(0,220)
ax.grid(True, linestyle="--", linewidth=1, color="black")
ax.plot(month, gangnam, color="red", label="Gangnam", marker="^", )
ax.plot(month, hongdae, color="blue", label="Hongdae", marker="o",)
ax.set_ylabel("매출")
ax.set_xlabel("월")
ax.legend()


plt.show()

