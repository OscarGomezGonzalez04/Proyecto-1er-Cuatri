from countries_population1 import *


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
    
   
    
