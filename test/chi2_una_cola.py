import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# definimos los parámetros de la distribución chi-cuadrado
df = 9

# definimos el nivel de significancia
alpha = 0.05

# definimos el rango de valores para la variable aleatoria
x = np.linspace(0, chi2.ppf(0.999, df), 1000)

# definimos la función de densidad de probabilidad de la distribución chi-cuadrado
pdf = chi2.pdf(x, df)

# Valor crítico de la chi-cuadrado a la izquierda
valor_critico = chi2.ppf(alpha, df)

# definimos los límites del área de rechazo
limite_izquierdo = x[x <= valor_critico]
limite_derecho = x[x >= valor_critico]

# creamos la figura y los ejes
fig, ax = plt.subplots()

# graficamos la función de densidad de probabilidad
ax.plot(x, pdf)

# sombrear el área de rechazo a la derecha del valor crítico
ax.fill_between(limite_derecho, 0, chi2.pdf(limite_derecho, df), alpha=0.5, label="Rechazo {}".format(valor_critico))

# sombrear el área de rechazo a la izquierda del valor crítico
ax.fill_between(limite_izquierdo, 0, chi2.pdf(limite_izquierdo, df), alpha=0.5, label="Rechazo {}".format(valor_critico))

# ajustamos los límites de los ejes
ax.set_xlim([0, chi2.ppf(0.999, df)])
ax.set_ylim([0, max(pdf)*1.1])

# Graficar la línea vertical
ax.axvline(x=18.13, color='red', label="X^2 = {}".format(18.13))

# mostramos la leyenda
ax.legend(loc="best")

# mostramos la figura
plt.show()