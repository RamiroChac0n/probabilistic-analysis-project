import numpy as np
import matplotlib.pyplot as plt

df = 5
x = np.linspace(0, 20, 1000)
y = np.power(x, (df/2)-1) * np.exp(-x/2) / (np.power(2, df/2) * np.math.gamma(df/2))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la línea vertical


# Graficar la curva 1 en los ejes
ax.plot(x, y, color='blue')

# Definir los límites de las áreas a sombrear
x_left = 1
x_right = 7.5

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= x_left), color='blue', alpha=0.3)

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= x_right), color='blue', alpha=0.3)

# Graficar la línea vertical
ax.axvline(x=5, color='red')

plt.title('Distribución chi-cuadrado con df = {}'.format(df))
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.show()