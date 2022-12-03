from countries_population1 import *
from matplotlib import pyplot as plt

#Nos muestra la gráfica del flujo del porcentaje del incremento de población a lo largo de los años
def graf_incremento_poblacion(registros, pais):
    a = [i for i, _ in incremento_poblacion(registros, pais)]
    b = [u for _, u in incremento_poblacion(registros, pais)]
    plt.plot(a, b, color = 'blue', linewidth=3, label= 'Porcentaje del incremento de la población')
    plt.legend()
    plt.show()
