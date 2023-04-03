import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def una_cola_izquierda(muestra, desviacion_std_muestral, desviacion_std_poblacional, alpha):
    # definimos los parámetros de la distribución chi-cuadrado
    grados_libertad = len(muestra) - 1

    chi2_prueba = (muestra - 1) * (desviacion_std_muestral / desviacion_std_poblacional) ** 2

    # definimos el rango de valores para la variable aleatoria
    x = np.linspace(0, chi2.ppf(0.999, grados_libertad), 1000)

    # definimos la función de densidad de probabilidad de la distribución chi-cuadrado
    pdf = chi2.pdf(x, grados_libertad)

    # Valor crítico de la chi-cuadrado a la izquierda
    valor_critico = chi2.ppf(alpha, grados_libertad)

    # definimos los límites del área de rechazo
    limite_izquierdo = x[x <= valor_critico]

    # creamos la figura y los ejes
    fig, ax = plt.subplots()

    # graficamos la función de densidad de probabilidad
    ax.plot(x, pdf)

    # sombrear el área de rechazo a la derecha del valor crítico
    ax.fill_between(limite_izquierdo, 0, chi2.pdf(limite_izquierdo, grados_libertad), alpha=0.5, label="Rechazo {}".format(valor_critico))

    # ajustamos los límites de los ejes
    ax.set_xlim([0, chi2.ppf(0.999, grados_libertad)])
    ax.set_ylim([0, max(pdf)*1.1])

    # Graficar la línea vertical
    ax.axvline(x=chi2_prueba, color='red', label="X^2 = {}".format(chi2_prueba))

    # Calcular el P-valor
    p_valor = chi2.cdf(chi2_prueba, grados_libertad)

    # Sombrear el area del P-valor sin mezclar con el area de rechazo
    ax.fill_between(x, 0, chi2.pdf(x, grados_libertad), where=(x <= chi2_prueba), alpha=0.5, color='skyblue', label="P-valor = {}".format(p_valor))

    # mostramos la leyenda
    ax.legend(loc="best")
    plt.savefig('grafica.jpg')