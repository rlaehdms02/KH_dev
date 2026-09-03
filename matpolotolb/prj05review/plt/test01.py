import matplotlib.pyplot as plt
import numpy as np

# 1. 데이터 준비
round_  = ["1회", "2회", "3회", "4회", "5회", "6회"]
class_a = [62, 70, 68, 75, 82, 88]   # A반
class_b = [55, 64, 72, 70, 78, 85]   # B반

# 2. 한글 폰트 설정 (Windows 기본 폰트)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 3. 차트 생성
fig, ax = plt.subplots(figsize=(10, 6))

# 두 반 꺾은선 그래프
ax.plot(round_, class_a, marker="s", label="A반", color="#1f77b4", linewidth=2)
ax.plot(round_, class_b, marker="o", label="B반", color="#ff7f0e", linewidth=2, linestyle="--")

# 회차별 두 반의 평균 선 추가
avg_list = (np.array(class_a) + np.array(class_b)) / 2
ax.plot(round_, avg_list, marker="^", label="월별 평균", color="#2ca02c", linewidth=2, linestyle=":", markersize=8)

# 범례 및 격자(Grid) 설정
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, alpha=0.5, linestyle="--")

# 축 이름 및 Y축 범위 설정 (0부터 시작)
ax.set_xlabel("회차", fontsize=11, labelpad=8)
ax.set_ylabel("점수", fontsize=11, labelpad=8)
ax.set_ylim(0, 100)

# 전체 평균 계산 및 제목 표시
total_list = class_a + class_b
total_avg = np.mean(total_list)
ax.set_title(f"회차별 평균 점수 추이 (전체 평균 {total_avg:.1f}점수)", fontsize=13, fontweight="bold", pad=12)

# 4. 최고 점수 반 및 회차 탐색
max_val_a = max(class_a)
max_val_b = max(class_b)

if max_val_a >= max_val_b:
    max_val = max_val_a
    max_round = round_[class_a.index(max_val)]
    max_branch = "class_a"
else:
    max_val = max_val_b
    max_round = round_[class_b.index(max_val)]
    max_branch = "class_b"

# 5. 최고 점수 주석(annotate) 표시
ax.annotate(
    f"최고 점수 {max_val}점 ({max_branch})",
    xy=(max_round, max_val),
    xytext=("회차", max_val+10),
    arrowprops=dict(arrowstyle="->", color="purple", lw=1.5),
    fontweight="bold",
    fontsize=10,
    color="purple",
    bbox=dict(boxstyle="round,pad=0.3", fc="#f3e5f5", ec="purple", lw=1)
)

plt.tight_layout()

# 6. 이미지 저장 및 출력
plt.savefig("result.png", dpi=300)
plt.show()
