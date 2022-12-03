from countries_population1 import *
from countries_population2 import *


#----Test de funciones----#
def test_lee_fichero(datos):
    #La función recibe unos datos(en este caso, correspondientes a los países dados) obtenidos de la función 'lee_fichero'
    print("----Test de la función: lee_fichero----")
    print("")
    print("El número total de registros leídos es ", len(datos))
    print("")
    print("Los tres primeros registros leídos de esta función son:", datos[:3])
    print("")
    print("Los tres últimos registros leídos de esta función son:", datos[-3:])
    
#-------BLOQUE 1-------
def test_calcula_paises(registros):
    print("\n----Test de la función: calcula_paises----")
    print("Hay ", len(calcula_paises(registros)))

def test_media_poblacion_cada_pais(registros):
    print("\n----Test de la función: media_poblacion_cada_pais----")
    print("La media de población de cada país es:", media_poblacion_cada_pais(registros))

#-------BLOQUE 2-------

def test_filtra_paises_por_media_edad(registros, filtro):
    print("\n----Test de la función: filtra_paises_por_media_edad----")
    print("Los países con una tasa de edad promedio inferior a", filtro," son:", filtra_paises_por_media_edad(registros, filtro))
def test_min_pais_por_edad_media(registros, filtro):
    print("\n----Test de la función: min_pais_por_edad_media----")
    print("El pais con menor media de edad es", min_pais_por_edad_media(registros, filtro))
def test_ordenar_paises_por_edad_media(registros, filtro):
    print("\n-----Test de la función: ordenar_paises_por_edad_media----")
    print("Estos son los países ordenados de mayor a menor según su edad media:", ordenar_paises_por_edad_media(registros, filtro)) 
def test_agrupar_paises_por_ranking(registros):
    print("\n----Test de la función: agrupar_paises_por_ranking----")
    print("Estos son todos los países con sus respectivos puestos en el ranking mundial:", agrupar_paises_por_ranking(registros))

#-------BLOQUE 3-------
def test_contar_poblacion_por_pais(registros):
    print("\n----Test de la función: contar_poblacion_por_pais----")
    print(contar_poblacion_por_pais(registros))
def test_min_año_mencionado(registros):
    print("\n----Test de la función: min_año_mencionado----")
    print(min_año_mencionado(registros))
def test_dicc_porcentaje_poblacion_por_anyo(registros, pais):
    print("\n----Test de la función: dicc_porcentaje_poblacion_por_anyo----")
    print(dicc_porcentaje_poblacion_por_anyo(registros, pais))
def test_incremento_poblacion(registros, pais):
    print("\n----Test de la función: incremento_poblacion----")
    lista = incremento_poblacion(registros, pais)
    for e, s in lista:
        print("{:3d} -> {:6.3f}".format(e, s), end='')
    
#-------BLOQUE 4-------
def test_graf_incremento_poblacion(registros, pais):
    print("\n----Test de la función: graf_incremento_poblacion----")
    print(graf_incremento_poblacion(registros, pais))

#----Bloque principal----#
if __name__ == "__main__":
    DATOS = lee_fichero('./data/countries_population.csv')
    test_lee_fichero(DATOS)
    test_calcula_paises(DATOS)
    test_media_poblacion_cada_pais(DATOS)
    test_filtra_paises_por_media_edad(DATOS, 15)
    test_min_pais_por_edad_media(DATOS, 15)
    test_ordenar_paises_por_edad_media(DATOS, 15)
    test_agrupar_paises_por_ranking(DATOS)
    test_contar_poblacion_por_pais(DATOS)
    test_min_año_mencionado(DATOS)
    test_dicc_porcentaje_poblacion_por_anyo(DATOS, 'Seychelles')
    test_incremento_poblacion(DATOS, 'China')
    test_graf_incremento_poblacion(DATOS, 'China')
   
    
