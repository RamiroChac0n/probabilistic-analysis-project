import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

def valor_observado(media_muestral, media_poblacional, desviacion_std_muestral, muestra):
    return (media_muestral - media_poblacional) / (desviacion_std_muestral / np.sqrt(muestra));

def dos_colas(media_muestral, media_poblacional, desviacion_std_muestral, muestra, alpha, valor_esperado):

    grados_libertad = muestra - 1;

    t_prueba = valor_observado(media_muestral, media_poblacional, desviacion_std_muestral, muestra);

    # Crear un conjunto de valores x en el rango de -4 a 4 con incrementos de 0.1
    x = np.arange(-4, 4, 0.1)

    # Definir el valor crítico
    t_critico_inferior = t.ppf(alpha/2, grados_libertad)
    t_critico_superior = t.ppf(1 - (alpha/2), grados_libertad)

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar la función de densidad de probabilidad
    ax.plot(x, t.pdf(x, grados_libertad), 'blue')

    # Graficar la línea vertical
    ax.axvline(x=0, color='black', linewidth = 1)

    # Sombrear el área a la izquierda del valor crítico
    plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x<=t_critico_inferior, color='blue', alpha=0.5, label = "tc Inferior = {}".format(t_critico_inferior))

    plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x>=t_critico_superior, color='blue', alpha=0.5, label = "tc Superior = {}".format(t_critico_superior))

    # Graficar la línea vertical
    ax.axvline(x=t_prueba, color='red', label="tp = {}".format(t_prueba))

    if valor_esperado == True:
        if t_prueba > 0:
            # Calcular el P-valor
            p_valor = t.sf(t_prueba, grados_libertad)

            # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x>=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

            # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x<=-t_prueba, color='skyblue', alpha=0.5)
        else:
            # Calcular el P-valor
            p_valor = t.cdf(t_prueba, grados_libertad)

            # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x<=t_prueba, color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

            # Sombrear el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, t.pdf(x, grados_libertad), where=x>=-t_prueba, color='skyblue', alpha=0.5)

    plt.legend()
    plt.savefig('grafica.jpg')