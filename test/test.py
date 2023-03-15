import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

alpha = 0.05

# Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
x = np.arange(-3, 3, 0.1)

# Crear la distribución normal
y = norm.pdf(x, 5, 1)

# Graficar la distribución normal
fig, ax = plt.subplots()
ax.plot(x, y)

z_critico_inferior = norm.ppf(alpha/2)
z_critico_superior = norm.ppf(1-alpha/2)

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))

# Graficar la línea vertical
ax.axvline(x=-1.24, color='red', label = "Zp = {}".format(-1.24))

plt.xlabel('Valores x')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.title('Distribución normal estándar')
plt.show()
