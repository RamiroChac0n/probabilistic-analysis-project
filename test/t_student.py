import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Definir los grados de libertad
df = 10
alpha = 0.1
# Generar una muestra aleatoria de la distribución t
x = np.linspace(t.ppf(0.01, df), t.ppf(0.99, df), 100)

# Definir el valor crítico
t_critico_inferior = t.ppf(alpha/2, df)
t_critico_superior = t.ppf(1 - (alpha/2), df)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función de densidad de probabilidad
ax.plot(x, t.pdf(x, df), 'blue')

# Graficar la línea vertical
ax.axvline(x=0, color='black')

# Sombrear el área a la izquierda del valor crítico
plt.fill_between(x, 0, t.pdf(x, df), where=x<=t_critico_inferior, color='blue', alpha=0.3)

plt.fill_between(x, 0, t.pdf(x, df), where=x>=t_critico_superior, color='blue', alpha=0.3)

# Graficar la línea vertical
ax.axvline(x=-1.24, color='red')

plt.legend()
plt.show()
