import csv
from collections import namedtuple
from datetime import datetime


Pais = namedtuple("Pais", "Month, Year, Date, Country, Population, Yearly_Change, Anual_changes, Migrants, Median_Age, Fertility_Rate, Density, city_Popu, Urban_Populations , Countrys_Share_of_World_Pop , Global_community, Rank, War, Partner")

def lee_fichero(fichero):
        #La función recibe como parámetro un fichero
    with open(fichero, encoding="utf-8") as f:
        #Abrimos el fichero con "utf-8", pues es el formato más recomendable para el tipo de archivos con los que trabajamos
        lector = csv.reader(f, delimiter= ",")
        #Leemos el fichero separando cada linea usando "," como delimitador, aunque realmente al tratarse de un csv no sería necesario
        next(lector)
        next(lector)
        #Al tratarse de un archivo csv, es recomendable saltar la cabecera que este tipo de archivos suelen presentar
        datos=[]
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
            Global_community=listado[14]
            Rank=listado[15]
            War=bool(listado[16])
            Partner=listado[17]
        #Creamos una lista a la cual añadimos tuplas(cada país) mediante un for, a la vez que asignamos a cada elemento de la tupla su correspondiente tipo de dato
            tupla=Pais(Month, Year, Date, Country, Population, Yearly_Change, Anual_changes, Migrants, Median_Age, Fertility_Rate, Density, city_Popu, Urban_Populations , Countrys_Share_of_World_Pop , Global_community, Rank, War, Partner)
            datos.append(tupla)
    return datos

    #La función nos devuelve una lista de tuplas equivalente a toda la información del fichero dado







 



        


