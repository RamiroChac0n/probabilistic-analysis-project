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
ax.plot(x, y, 'blue')

# Establecer los márgenes de la figura para centrar la gráfica
ax.margins(x=0, y=0.1)

# Graficar la línea vertical
ax.axvline(x=mu, color='black')

# Definir los límites de las áreas a sombrear
z_critico_inferior = -2.58
z_critico_superior = 2.58

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Área de rechazo")

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3)

# Graficar la línea vertical
ax.axvline(x=-1.24, color='red', label = "Zp = {}".format(-1.24))

plt.title('Función Gaussiana')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()