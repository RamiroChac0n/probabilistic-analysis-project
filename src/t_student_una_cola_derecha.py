import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

def una_cola_derecha(media_muestral, media_poblacional, desviacion_std_muestral, muestra, alpha, valor_esperado):

    grados_libertad = len(muestra) - 1

    t_prueba = valor_observado(media_muestral, media_poblacional, desviacion_std_muestral, muestra);

    # Crear un conjunto de valores x en el rango de -4 a 4 con incrementos de 0.1
    x = np.arange(-4, 4, 0.01)

    # Definir el valor crítico
    t_critico = t.ppf(1-alpha, grados_libertad)

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar la función de densidad de probabilidad
    ax.plot(x, t.pdf(x, grados_libertad), 'blue')

    # Graficar la línea vertical
    ax.axvline(x=0, color='black', linewidth = 1)

    # Sombrear el área a la izquierda del valor crítico
    plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x>=t_critico, color='blue', alpha=0.5, label = "tc Superior = {}".format(t_critico))

    if valor_esperado == True:
        # Graficar la línea vertical
        ax.axvline(x=t_prueba, color='red', label="tp = {}".format(t_prueba))

        # Calcula el P-valor
        p_valor = t.sf(t_prueba, grados_libertad)

        # Sombrea el area del P-valor sin mezclar con el area de la cola
        plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x>=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    plt.legend()
    plt.savefig('grafica.jpg')

def valor_observado(media_muestral, media_poblacional, desviacion_std_muestral, muestra):
    return (media_muestral - media_poblacional) / (desviacion_std_muestral / np.sqrt(muestra));