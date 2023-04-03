import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def dos_colas(muestra, desviacion_std_muestral, desviacion_std_poblacional, alpha):

    grados_libertad = len(muestra) - 1

    chi2_prueba = (muestra - 1) * (desviacion_std_muestral / desviacion_std_poblacional) ** 2

    # definimos el rango de valores para la variable aleatoria
    x = np.linspace(0, chi2.ppf(0.999, grados_libertad), 1000)

    # definimos la función de densidad de probabilidad de la distribución chi-cuadrado
    pdf = chi2.pdf(x, grados_libertad)

    # Valor crítico de la chi-cuadrado a la izquierda
    left_critical_value = chi2.ppf(alpha/2, grados_libertad)

    # Valor crítico de la chi-cuadrado a la derecha
    right_critical_value = chi2.ppf(1 - alpha/2, grados_libertad)

    # definimos los límites del área de rechazo
    left_limit = x[x <= left_critical_value]
    right_limit = x[x >= right_critical_value]

    # creamos la figura y los ejes
    fig, ax = plt.subplots()

    # graficamos la función de densidad de probabilidad
    ax.plot(x, pdf)

    # sombrear el área de rechazo a la derecha del valor crítico
    ax.fill_between(right_limit, 0, chi2.pdf(right_limit, grados_libertad), alpha=0.5, label="Rechazo {}".format(right_critical_value))

    # sombrear el área de rechazo a la izquierda del valor crítico
    ax.fill_between(left_limit, 0, chi2.pdf(left_limit, grados_libertad), alpha=0.5, label="Rechazo {}".format(left_critical_value))

    # ajustamos los límites de los ejes
    ax.set_xlim([0, chi2.ppf(0.999, grados_libertad)])
    ax.set_ylim([0, max(pdf)*1.1])

    # Graficar la línea vertical
    ax.axvline(x=chi2_prueba, color='red', label="X^2 = {}".format(chi2_prueba))

    # mostramos la leyenda
    ax.legend(loc="best")
    plt.savefig('grafica.jpg')