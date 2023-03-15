import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Definir grados de libertad y crear un conjunto de valores para x
df = 120
x = np.linspace(0, 20, 500)

# Calcular los valores de la función chi-cuadrado para diferentes valores de x
y = chi2.pdf(x, df)

# creamos la figura y los ejes
fig, ax = plt.subplots()

# Graficar la función chi-cuadrado
ax.plot(x, y, 'b-', label='Grados de Libertad: %d' % df)

# Rellenar el área bajo la curva para pruebas de hipótesis de 2 colas
critical_value = chi2.ppf(0.975, df)
x1 = np.linspace(critical_value, 20, 100)
y1 = chi2.pdf(x1, df)
plt.fill_between(x1, y1, 0, color='blue', alpha=0.1)
x2 = np.linspace(0, chi2.ppf(0.025, df), 100)
y2 = chi2.pdf(x2, df)
plt.fill_between(x2, y2, 0, color='blue', alpha=0.1)

# ajustamos los límites de los ejes
ax.set_xlim([0, chi2.ppf(0.999, df)])
ax.set_ylim([0, max(y)*1.1])

# Configurar el gráfico
plt.xlim(0, 20)
plt.ylim(0, 0.3)
plt.xlabel('Valores Chi-cuadrado')
plt.ylabel('Probabilidad')
plt.title('Función Chi-cuadrado para pruebas de hipótesis de 2 colas')
plt.legend()

# Mostrar el gráfico
plt.show()
