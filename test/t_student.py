import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Definir los grados de libertad
gl = 5
alpha = 0.1
# Generar una muestra aleatoria de la distribución t
x = np.linspace(t.ppf(0.01, gl), t.ppf(0.99, gl), 100)

# Definir el valor crítico
t_critico_inferior = t.ppf(alpha/2, gl)
t_critico_superior = t.ppf(1 - (alpha/2), gl)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función de densidad de probabilidad
ax.plot(x, t.pdf(x, gl), 'blue')

# Graficar la línea vertical
ax.axvline(x=0, color='black')

# Sombrear el área a la izquierda del valor crítico
plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_critico_inferior, color='blue', alpha=0.3, label = "Área de rechazo")

plt.fill_between(x, 0, t.pdf(x, gl), where=x>=t_critico_superior, color='blue', alpha=0.3)

# Graficar la línea vertical
ax.axvline(x=-1.24, color='red', label="tp = {}".format(-1.24))

plt.legend()
plt.show()
