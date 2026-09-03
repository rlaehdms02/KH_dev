import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# data
lang = ["python", "java", "cpp", "c", "rust"]
ratio = [25,3,2,2,7]
fig, ax = plt.subplots(figsize=(8, 6))

# 파이차트
ax.pie(ratio, labels = lang, autopct = "%1.1f%%", startangle = 90)
ax.set_title("pie chart")
plt.show()