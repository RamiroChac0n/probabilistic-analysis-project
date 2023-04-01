import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Definir los grados de libertad
gl = 26
alpha = 0.01
t_prueba = -1.53

# Crear un conjunto de valores x en el rango de -4 a 4 con incrementos de 0.1
x = np.arange(-4, 4, 0.01)

# Definir el valor crítico
t_critico = t.ppf(alpha, gl)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función de densidad de probabilidad
ax.plot(x, t.pdf(x, gl), 'blue')

# Graficar la línea vertical
ax.axvline(x=0, color='black', linewidth = 1)

# Sombrear el área a la izquierda del valor crítico
plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_critico, color='blue', alpha=0.3, label = "tc Inferior = {}".format(t_critico))

# Graficar la línea vertical
ax.axvline(x=t_prueba, color='red', label="tp = {}".format(t_prueba))

# Calcula el P-valor
p_valor = t.cdf(t_prueba, gl)

# Sombrea el area del P-valor sin mezclar con el area de la cola
plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

plt.legend()
plt.show()