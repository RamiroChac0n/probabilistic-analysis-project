import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def valor_observado_proporciones(p_m, p, n, q):
    return (p_m - p) / np.sqrt((p * q) / n);

def valor_observado(x_m, mu, sigma, n):
    return (x_m - mu) / (sigma / np.sqrt(n));

def una_cola_derecha(media_muestral, media_poblacional, desviacion_std_poblacional, muestra, alpha, valor_esperado):

    z_prueba = valor_observado(media_muestral, media_poblacional, desviacion_std_poblacional, muestra)

    # Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
    x = np.arange(-4, 4, 0.01)

    # Crear la distribución normal
    y = norm.pdf(x, 0, 1)

    # Graficar la distribución normal
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Graficar la línea vertical
    ax.axvline(0, color='black', linewidth = 1)

    z_critico = norm.ppf(1-alpha)

    # Sombrar el área derecha debajo de la curva
    plt.fill_between(x, 0, y, where=(x >= z_critico), color='blue', alpha=0.3, label = "Zc = {}".format(z_critico))

    if valor_esperado == True:
        # Graficar la línea vertical
        ax.axvline(x=z_prueba, color='red', label = "Zp = {}".format(z_prueba))

        # Calcula el P-valor
        p_valor = 1 - norm.cdf(z_prueba)

        # Sombrea el area del P-valor incluyendo el valor critico sin mezclar con el area de la cola
        plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    plt.legend()
    plt.xlabel('Valores x')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución normal estándar')
    plt.savefig('grafica.jpg')

def una_cola_derecha_proporciones(proporcion_muestral, proporcion_poblacional, muestra, alpha, valor_esperado):

    z_prueba = valor_observado_proporciones(proporcion_muestral, proporcion_poblacional, muestra, 1 - proporcion_poblacional)

    # Crear un conjunto de valores x en el rango de -4 a 4 con incrementos de 0.01
    x = np.arange(-4, 4, 0.01)

    # Crear la distribución normal
    y = norm.pdf(x, 0, 1)

    # Graficar la distribución normal
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Graficar la línea vertical
    ax.axvline(0, color='black', linewidth = 1)

    z_critico = norm.ppf(1-alpha)

    # Sombrar el área derecha debajo de la curva
    plt.fill_between(x, 0, y, where=(x >= z_critico), color='blue', alpha=0.5, label = "Zc = {}".format(z_critico))

    if valor_esperado == True:
        # Graficar la línea vertical
        ax.axvline(x=z_prueba, color='red', label = "Pp = {}".format(z_prueba))

        # Calcula el P-valor
        p_valor = 1 - norm.cdf(z_prueba)

        # Sombrea el area del P-valor incluyendo el valor critico sin mezclar con el area de la cola
        plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    plt.legend()
    plt.xlabel('Valores x')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución normal estándar')
    plt.savefig('grafica.jpg')