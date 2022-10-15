from countries_population1 import *


#----Test de funciones----#
def test_lee_fichero(Paises):
    #La función recibe unos datos(en este caso, correspondientes a los países dados) obtenidos de la función 'lee_fichero'
    print("----Test de la función: lee_fichero----")
    print("")
    print("El número total de registros leídos es ", len(Paises))
    print("")
    print("Los tres primeros registros leídos de esta función son:", Paises[:3])
    print("")
    print("Los tres últimos registros leídos de esta función son:", Paises[-3:])
    







    



#----Bloque principal----#
if __name__ == "__main__":
    datos = lee_fichero('./data/countries_population.csv')
    test_lee_fichero(datos)
   
    
