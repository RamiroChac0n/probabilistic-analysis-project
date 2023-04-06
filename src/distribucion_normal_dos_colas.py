import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def valor_observado_proporciones(p_m, p, n, q):
    return (p_m - p) / np.sqrt((p * q) / n);

def valor_observado(x_m, mu, sigma, n):
    return (x_m - mu) / (sigma / np.sqrt(n));

def dos_colas(media_muestral, media_poblacional, desviacion_std_poblacional, muestra, alpha, valor_esperado):

    z_prueba = valor_observado(media_muestral, media_poblacional, desviacion_std_poblacional, muestra);

    # Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
    x = np.arange(-4, 4, 0.1)

    # Crear la distribución normal
    y = norm.pdf(x, 0, 1)

    # Graficar la distribución normal
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Graficar la línea vertical
    ax.axvline(0, color='black', linewidth = 1)

    z_critico_inferior = norm.ppf(alpha/2)
    z_critico_superior = norm.ppf(1-alpha/2)

    # Sombrar el área izquierda debajo de la curva
    plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.5, label = "Zc Inferior = {}".format(z_critico_inferior))

    # Sombrar el área derecha debajo de la curva
    plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.5, label = "Zc Superior = {}".format(z_critico_superior))

    if valor_esperado == True:
        # Graficar la línea vertical
        ax.axvline(x=z_prueba, color='red', label = "Zp = {}".format(z_prueba))

        if z_prueba > 0:
            # Calcular el P-valor
            p_valor = norm.sf(z_prueba)

            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, y, where=(x <= -z_prueba), color='skyblue', alpha=0.5)
        else:
            # Calcular el P-valor
            p_valor = norm.cdf(z_prueba)

            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, y, where=(x <= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, y, where=(x >= -z_prueba), color='skyblue', alpha=0.5)

    plt.legend()
    plt.xlabel('Valores x')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución normal estándar')
    plt.savefig('grafica.jpg')


def dos_colas_proporciones(proporcion_muestral, proporcion_poblacional, muestra, alpha, valor_esperado):
    
    p = proporcion_poblacional
    q = 1 - p
    p_m = proporcion_muestral
    n = muestra
    
    z_prueba = valor_observado_proporciones(p_m, p, n, q);
    
    # Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
    x = np.arange(-4, 4, 0.1)
    
    # Crear la distribución normal
    y = norm.pdf(x, 0, 1)
    
    # Graficar la distribución normal
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # Graficar la línea vertical
    ax.axvline(0, color='black', linewidth = 1)
    
    z_critico_inferior = norm.ppf(alpha/2)
    z_critico_superior = norm.ppf(1-alpha/2)
    
    # Sombrar el área izquierda debajo de la curva
    plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.5, label = "Zc Inferior = {}".format(z_critico_inferior))
    
    # Sombrar el área derecha debajo de la curva
    plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.5, label = "Zc Superior = {}".format(z_critico_superior))
    
    if valor_esperado == True:
        # Graficar la línea vertical
        ax.axvline(x=z_prueba, color='red', label = "Zp = {}".format(z_prueba))
    
        if z_prueba > 0:
            # Calcular el P-valor
            p_valor = norm.sf(z_prueba)
    
            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))
    
            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, y, where=(x <= -z_prueba), color='skyblue', alpha=0.5)
        else:
            # Calcular el P-valor
            p_valor = norm.cdf(z_prueba)
    
            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
            plt.fill_between(x, 0, y, where=(x <= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))
    
            # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
            plt.fill_between(x, 0, y, where=(x >= -z_prueba), color='skyblue', alpha=0.5)
    plt.legend()
    plt.xlabel('Valores x')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución normal estándar')
    plt.savefig('grafica.jpg')