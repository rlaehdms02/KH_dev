import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

fix, axex = plt.subplots(2, 2, figsize=(10,5))
fix.suptitle("4개 그래프")
plt.tight_layout()

x = np.linspace(0,10, 100)
axex[0][0].plot(x, np.sin(x))
axex[0][0].set_title("sin 그래프")
axex[0][1].plot(x, np.cos(x))
axex[0][1].set_title("cos 그래프")
axex[1][0].plot(x, x**2)
axex[1][0].set_title("x**2 그래프")
axex[1][1].plot(x, np.sqrt(x))
axex[1][1].set_title("sqrt 그래프")

fix.show()