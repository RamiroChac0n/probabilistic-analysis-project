import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la función gaussiana
mu = 0
sigma = 1

# Crear un vector de datos x desde -4 a 4 en incrementos de 0.1
x = np.arange(-4, 4, 0.1)

# Calcular los valores de la función gaussiana para los datos x
y = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la curva 1 en los ejes
ax.plot(x, y, color='blue')

# Establecer los márgenes de la figura para centrar la gráfica
ax.margins(x=0, y=0.1)

# Graficar la línea vertical
ax.axvline(x=mu, color='black')

# Graficar la línea vertical
ax.axvline(x=-1.24, color='red')

# Definir los límites de las áreas a sombrear
x_left = -2.58
x_right = 2.58

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= x_left), color='blue', alpha=0.3)

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= x_right), color='blue', alpha=0.3)

plt.title('Función Gaussiana')
plt.xlabel('x')
plt.ylabel('y')
plt.show()