import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Definir los grados de libertad
gl = 24
alpha = 0.05

t_prueba = -1.667

# Crear un conjunto de valores x en el rango de -4 a 4 con incrementos de 0.1
x = np.arange(-4, 4, 0.1)

# Definir el valor crítico
t_critico_inferior = t.ppf(alpha/2, gl)
t_critico_superior = t.ppf(1 - (alpha/2), gl)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función de densidad de probabilidad
ax.plot(x, t.pdf(x, gl), 'blue')

# Graficar la línea vertical
ax.axvline(x=0, color='black', linewidth = 1)

# Sombrear el área a la izquierda del valor crítico
plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_critico_inferior, color='blue', alpha=0.3, label = "tc Inferior = {}".format(t_critico_inferior))

plt.fill_between(x, 0, t.pdf(x, gl), where=x>=t_critico_superior, color='blue', alpha=0.3, label = "tc Superior = {}".format(t_critico_superior))

# Graficar la línea vertical
ax.axvline(x=t_prueba, color='red', label="tp = {}".format(t_prueba))

if t_prueba > 0:
    # Calcular el P-valor
    p_valor = t.sf(t_prueba, gl)

    # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola superior
    plt.fill_between(x, 0, t.pdf(x, gl), where=x>=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola inferior
    plt.fill_between(x, 0, t.pdf(x, gl), where=x<=-t_prueba, color='skyblue', alpha=0.5)
else:
    # Calcular el P-valor
    p_valor = t.cdf(t_prueba, gl)

    # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola superior
    plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola inferior
    plt.fill_between(x, 0, t.pdf(x, gl), where=x>=-t_prueba, color='skyblue', alpha=0.5)

plt.legend()
plt.show()
