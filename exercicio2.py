import numpy as np
import matplotlib.pyplot as plt

# Array x de -100 a 100
x = np.arange(-100, 101)

# gráfico: f(x) = 2x + 4
f1 = 2 * x + 4
plt.figure()
plt.plot(x, f1)
plt.title("f(x) = 2x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("f1_linear.png", dpi=300, bbox_inches="tight")  # <- salva aqui
plt.show()

# gráfico: f(x) = 3x² - 2x - 8
f2 = 3 * x**2 - 2 * x - 8
plt.figure()
plt.plot(x, f2)
plt.title("f(x) = 3x² - 2x - 8")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("f2_quadratica.png", dpi=300, bbox_inches="tight")
plt.show()

# gráfico: f(x) = x³ - 3x² - x + 3
f3 = x**3 - 3 * x**2 - x + 3
plt.figure()
plt.plot(x, f3)
plt.title("f(x) = x³ - 3x² - x + 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("f3_cubica.png", dpi=300, bbox_inches="tight")
plt.show()
