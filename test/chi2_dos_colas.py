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
left_critical_value = chi2.ppf(alpha/2, df)

# Valor crítico de la chi-cuadrado a la derecha
right_critical_value = chi2.ppf(1 - alpha/2, df)

# definimos los límites del área de rechazo
left_limit = x[x <= left_critical_value]
right_limit = x[x >= right_critical_value]

# creamos la figura y los ejes
fig, ax = plt.subplots()

# graficamos la función de densidad de probabilidad
ax.plot(x, pdf)

# sombrear el área de rechazo a la derecha del valor crítico
ax.fill_between(right_limit, 0, chi2.pdf(right_limit, df), alpha=0.5, label="Rechazo {}".format(right_critical_value))

# sombrear el área de rechazo a la izquierda del valor crítico
ax.fill_between(left_limit, 0, chi2.pdf(left_limit, df), alpha=0.5, label="Rechazo {}".format(left_critical_value))

# ajustamos los límites de los ejes
ax.set_xlim([0, chi2.ppf(0.999, df)])
ax.set_ylim([0, max(pdf)*1.1])

# Graficar la línea vertical
ax.axvline(x=18.13, color='red', label="X^2 = {}".format(18.13))

# mostramos la leyenda
ax.legend(loc="best")

# mostramos la figura
plt.show()
