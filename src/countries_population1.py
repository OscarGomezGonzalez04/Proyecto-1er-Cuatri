import csv
from collections import namedtuple, defaultdict, Counter
from datetime import datetime
from parsers import *

Pais = namedtuple("Pais", "Month, Year, Date, Country, Population, Yearly_Change, Anual_changes, Migrants, Median_Age, Fertility_Rate, Density, city_Popu, Urban_Populations , Countrys_Share_of_World_Pop , Global_community, Rank, War, Partner")

def lee_fichero(fichero):
    result = []
    with open(fichero) as f:
        lector = csv.reader(f)
        next(lector)
        next(lector)
        for Month, Year, Date, Country, Population, Yearly_Change, Anual_changes, Migrants, Median_Age, Fertility_Rate, Density, city_Popu, Urban_Populations , Countrys_Share_of_World_Pop , Global_community, Rank, War, Partner in lector:
            result.append(Pais(int(Month.strip()), int(Year.strip()), parsea_fecha(Date.strip()), Country.strip(), int(Population.strip()), float(Yearly_Change.replace(",", ".").strip()), int(Anual_changes.strip()), int(Migrants.strip()), float(Median_Age.replace(",", ".").strip()), float(Fertility_Rate.replace(",", ".").strip()), float(Density.strip()), (float(city_Popu.replace(",", ".").strip()) if city_Popu != "" else city_Popu), (int(Urban_Populations.strip()) if Urban_Populations != "" else Urban_Populations ), float(Countrys_Share_of_World_Pop.replace(",", ".").strip()) , int(Global_community.strip()), int(Rank.strip()), parsea_boolean(War.strip()), Partner.strip()))
    return result

'''def lee_fichero(fichero):
        #La función recibe como parámetro un fichero
    with open(fichero, encoding="utf-8") as f:
        #Abrimos el fichero con "utf-8", pues es el formato más recomendable para el tipo de archivos con los que trabajamos
        lector = csv.reader(f, delimiter= ",")
        #Leemos el fichero separando cada linea usando "," como delimitador, aunque realmente al tratarse de un csv no sería necesario
        next(lector)
        next(lector)
        #Al tratarse de un archivo csv, es recomendable saltar la cabecera que este tipo de archivos suelen presentar
        registros=[]

    
        for listado in lector:
            Month=int(listado[0])
            Year=int(listado[1])
            Date=datetime.strptime(listado[2], "%d/%m/%Y")
            Country=listado[3]
            Population=int(listado[4])
            Yearly_Change=listado[5]
            Yearly_Change=Yearly_Change.replace(",", ".")
            Yearly_Change=float(Yearly_Change)
            Anual_changes=int(listado[6])
            Migrants=int(listado[7])
            Median_Age=listado[8]
            Median_Age=Median_Age.replace(",", ".")
            Median_Age=float(Median_Age)
            Fertility_Rate=listado[9]
            Fertility_Rate=Fertility_Rate.replace(",", ".")
            Fertility_Rate=float(Fertility_Rate)
            Density=float(listado[10])
            city_Popu=listado[11]
            city_Popu=city_Popu.replace(",", ".")
            if city_Popu != "":
             city_Popu=float(city_Popu)
            else:
                city_Popu=city_Popu
            if listado[12] != "":
                Urban_Populations=int(listado[12])
            else:
                Urban_Populations=listado[12]
        #En caso de que presenten espacio, habilitamos esta condicional para evitar problemas
            Countrys_Share_of_World_Pop=listado[13]
            Countrys_Share_of_World_Pop=Countrys_Share_of_World_Pop.replace(",", ".")
            Countrys_Share_of_World_Pop=float(Countrys_Share_of_World_Pop)
            Global_community= int(listado[14])
            Rank=listado[15]
            War=bool(listado[16])
            Partner=listado[17]
        #Creamos una lista a la cual añadimos tuplas(cada país) mediante un for, a la vez que asignamos a cada elemento de la tupla su correspondiente tipo de dato
            tupla=Pais(Month, Year, Date, Country, Population, Yearly_Change, Anual_changes, Migrants, Median_Age, Fertility_Rate, Density, city_Popu, Urban_Populations , Countrys_Share_of_World_Pop , Global_community, Rank, War, Partner)
            registros.append(tupla)
    return registros'''

    #La función nos devuelve una lista de tuplas equivalente a toda la información del fichero dado

#-------BLOQUE 1-------

#Función que devuelve un conjunto con los distintos paises cuya población supere los 50000000
def calcula_paises(registros):
    conjunto_paises = {r.Country for r in registros if r.Population > 50000000}
    return conjunto_paises

#Función que calcula la media de población de cada país
def media_poblacion_cada_pais(registros):
    res = defaultdict(list)

    for r in registros:
        clave = r.Country
        res[clave].append(r.Population)

    return {clave: sum(listado)/len(listado) for clave, listado in res.items()}
    
#-------BLOQUE 2-------
#Función auxiliar que obtiene un conjunto con los distintos países, la cual a su vez, incorporaremos en las siguientes funciones 
def filtra_paises_por_media_edad(registros, filtro):
    result = set()
    for r in registros:
      edad_media = r.Median_Age
      if edad_media < filtro:
        result.add((r.Country, r.Median_Age))

    
    return result 

#Función que incopora la función anterior(filtra_paises_por_media_edad) para calcular sobre el resultado de esta 
#el país con menor tasa de edad media
def min_pais_por_edad_media(registros, filtro):
    paises = filtra_paises_por_media_edad(registros, filtro)
    return min(paises, key= lambda x:x[1]) 

#Función que incopora la función anterior(filtra_paises_por_media_edad) para ordenar de mayor a menor los datos 
# obtenidos de esta en función de la edad media
def ordenar_paises_por_edad_media(registros, filtro):
    paises = filtra_paises_por_media_edad(registros, filtro)
    return sorted(paises, key= lambda x:x[1], reverse= True)

#Función que devuelve un diccionario cuyas claves son los países y los valores son los rankings que estos ocupan
# respecto al resto de países.
def agrupar_paises_por_ranking(registros):
    res = dict()
    for r in registros:
      clave = r.Country
      if clave in res:
         res[clave].add(r.Rank)
      else:
         res[clave] = set(r)
     
    return res


#-------BLOQUE 3-------

#Función que devuelve un diccionario que hace corresponder a cada clave(país) la 
# suma de sus poblaciones a lo largo de los distintos años incluidos en el csv
def contar_poblacion_por_pais(registros):
    res = dict()
    for r in registros:
        clave = r.Country
        if clave in res:
            res[clave]+=r.Population
        else:
            res[clave] = r.Population
    return res
#Función que devuelve el mínimo de un diccionario
#  que hace corresponder a cada clave(país) el número de tuplas que contienen dicha clave
def min_año_mencionado(registros):
    res = dict()
    for r in registros:
        clave = r.Year
        if clave in res:
            res[clave]+= 1
        else:
            res[clave] = 1
    return min(res.items(), key=lambda x:x[1])

#Función que devuelve un diccionario que hace corresponder a cada clave(año) el porcentaje 
# de población del país indicado respecto a la población global 

#Para ello, antes creamos una funcion auxiliar que nos devuelva una lista de tuplas(año, pob global) segun qué 
# país le indiquemos   

def poblacion_global_por_anyo(registros, pais):
    result = defaultdict(float)
    for r in registros:
        if pais == r.Country:

            result[r.Year] += r.Global_community
    return sorted(result.items(), reverse=True, key = lambda r:r[1])

def dicc_porcentaje_poblacion_por_anyo(registros, pais):
    result = defaultdict(float)
    anyos_poblaciones_glob={Year:glob for Year, glob in poblacion_global_por_anyo(registros, pais)}

    for r in registros:
        if pais == r.Country:

            result[r.Year] = 100 * r.Population/anyos_poblaciones_glob[r.Year]

    return result

#Función que devuelve una lista compuesta por tuplas(año actual, porcejntaje del
#  incremento de la población de un año para otro)

def incremento_poblacion(registros, pais):
    poblacion_global_por_anyo_ordenada = sorted(poblacion_global_por_anyo(registros, pais))
    var_auxiliar = list(zip(poblacion_global_por_anyo_ordenada[:-1], poblacion_global_por_anyo_ordenada[1:]))
    result = []
    for pob_anterior, pob_actual in var_auxiliar:
        result.append((pob_actual[0], 100.0*(pob_actual[1]-pob_anterior[1])/pob_anterior[1]))
    return result
        
    

    