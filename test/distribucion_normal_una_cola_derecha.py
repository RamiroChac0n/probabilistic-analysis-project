import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

alpha = 0.02
z_prueba = 1.14

# Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
x = np.arange(-4, 4, 0.1)

# Crear la distribución normal
y = norm.pdf(x, 0, 1)

# Graficar la distribución normal
fig, ax = plt.subplots()
ax.plot(x, y)

# Graficar la línea vertical
ax.axvline(0, color='black', linewidth = 1)

z_critico = norm.ppf(1-alpha)

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= z_critico), color='blue', alpha=0.3, label = "Zc = {}".format(z_critico))

# Graficar la línea vertical
ax.axvline(x=z_prueba, color='red', label = "Zp = {}".format(z_prueba))

# Calcula el P-valor
p_valor = 1 - norm.cdf(z_prueba)

# Sombrea el area del P-valor incluyendo el valor critico sin mezclar con el area de la cola
plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.3, label = "P-valor = {}".format(p_valor))

plt.legend()
plt.xlabel('Valores x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución normal estándar')
plt.show()