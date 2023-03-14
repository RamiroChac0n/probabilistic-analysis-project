import numpy as np
import matplotlib.pyplot as plt

gl = 5
x = np.linspace(0, 20, 1000)
y = np.power(x, (gl/2)-1) * np.exp(-x/2) / (np.power(2, gl/2) * np.math.gamma(gl/2))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la curva 1 en los ejes
ax.plot(x, y, color='blue')

# Definir los límites de las áreas a sombrear
chi2_critico_inferior = 1
chi2_critico_superior = 7.5

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= chi2_critico_inferior), color='blue', alpha=0.3, label = "Área de rechazo")

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= chi2_critico_superior), color='blue', alpha=0.3)

# Graficar la línea vertical
ax.axvline(x=5, color='red', label = "x^2 = {}".format(5))

plt.title('Distribución chi-cuadrado con gl = {}'.format(gl))
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.legend()
plt.show()