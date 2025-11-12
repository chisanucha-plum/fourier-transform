import matplotlib.pyplot as plt
import numpy as np

# สร้างแกน x
x = np.arange(0, 2 * np.pi, 0.01)

# 1.1 f(x) = sin(x) + (1/3)sin(2x)+(1/5)sin(4x)
f1 = np.sin(x) + (1 / 3) * np.sin(2 * x) + (1 / 5) * np.sin(4 * x)

# 1.2 f(x) = sin(x)+(1/5)sin(4x)+(1/9)sin(6x)
f2 = np.sin(x) + (1 / 5) * np.sin(4 * x) + (1 / 9) * np.sin(6 * x)

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(x, f1, "b", linewidth=1.5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.title("1)  f(x) = sin(x) + (1/3)sin(2x) + (1/5)sin(4x)")

plt.subplot(2, 1, 2)
plt.plot(x, f2, "r", linewidth=1.5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.title("2)  f(x) = sin(x) + (1/5)sin(4x) + (1/9)sin(6x)")

plt.tight_layout()
plt.show()
