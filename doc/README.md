# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \Óscar Gómez González\>   uvus:\oscgomgon\>
 
El proyecto tiene como objetivo analizar los datos de variabilidad de la población correspondiente a cada país entre 1955 y 2020 , publicados en el dataset de Kaggle , los cuales se pueden descargar de la siguiente URL (https://www.kaggle.com/datasets/themlphdstudent/countries-population-from-1955-to-2020). El dataset original tiene 17 columnas y 3550 filas , pero debido a la falta de un dato tipo date he decidido crear una nueva en la hoja de cáculo de Drive, llamada 'Date' , producto de concatenar ("1/";An;"/";Bn) + ALEATORIO.ENTRE(0;30) , siendo A la columna correspondiente al mes, y B la columna correspondiente al año. 
## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<countries_population1.py\>**: Está conformado por la asignación de una tupla con nombre , de la que hablaremos posteriormente, y por la definición de la función : 'lee_fichero' , de la que ,igualmente,, hablaremos más adelante
  * **\<countries_population_test.py\>**: Contiene funciones de test para probar las funciones del módulo countries_population1.py, además del main .
  * **\<countries_population2.py\>**:
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<countries_population.csv\>**: Es un dataset de tipo 'csv' compuesto de 3550 filas y 14 columnas, separadas por un ';' 
    * **\<dataset2.csv\>**:
    
## Estructura del *dataset*

El dataset contiene toda la información relevante a los países, la cual analizaremos y de la cual obtendremos una conclusión 
Este está compuesto por \<15\> columnas, con la siguiente descripción:
* **\<mes>**: de tipo \<int\>, representa el mes en el cual se data la correspondiente información
* **\<año>**: de tipo \<int\>, representa el año en el cual se data la correspondiente información
* **\<fecha>**: de tipo \<datetime\>, representa el dia, mes y año en el cual se data la correspondiente información
* **\<pais>**: de tipo \<str\>, representa el país al cual pertenecen dichos datos
* **\<poblacion>**: de tipo \<int\>, representa la población del país correspondiente
* **\<cambio_%_anual>**: de tipo \<float\>, representa el porcentaje del cambio producido en dicha población anualmente
* **\<cambio_anual>**: de tipo \<int\>, representa el cambio producido en dicha población anualmente
* **\<migrantes>**: de tipo \<int\>, representa el número de migrantes del país seleccionado
* **\<edad_media>**: de tipo \<float\>, representa la edad media del correspondiente país
* **\<tasa_fertilidad>**: de tipo \<float\>, representa la tasa de fertilidad del correspondiente país
* **\<densidad_población>**: de tipo \<float\>, representa la densidad demográfica de la población de cada país
* **\<porcentaje_poblacion_urbana>**: de tipo \<float\>, representa el porcentaje de población urbana respecto al total de esta
* **\<poblacion_urbana>**: de tipo \<int\>, representa la cantidad de población urbana
* **\<porcentaje_poblacion_mundial>**: de tipo \<float\>, representa el porcentaje que supone cada país respecto a la población mundial 
* **\<poblacion_mundial>**: de tipo \<int\>, representa el número de población mundial
* **\<ranking_mundial>**: de tipo \<int\>, representa la posición del país correspondiente en el ranking mundial en cuanto a población se refiere
* **\<guerra>**: de tipo \<bool\>, representa su posición en des/acuerdo frente a la guerra
* **\<aliado>**: de tipo \<str\>, representa el país aliado correspondiente al país a tratar
....

## Tipos implementados

He creado una namedtuple asociada a cada país , de manera que resulta más sencillo y práctico el acceso a los distintos elementos que conforman dichos países(tuplas)

## Funciones implementadas:

### \<countries_population1.py\>

* **<lee_fichero>**: La función recibe como parámetro un fichero , el cual abre leyendo el fichero separando cada linea usando "," como delimitador. A continuación, crea una lista a la cual añadimos tuplas(cada país) mediante un for, a la vez que asignamos a cada elemento de la tupla su correspondiente tipo de dato , de manera que finalmente devuelve dicha lista
* **<calcula_paises>**:Función que devuelve un conjunto con los distintos paises cuya población supere los 50000000
* **<media_poblacion_cada_pais>**:Función que calcula la media de población de cada país
* **<filtra_paises_por_media_edad>**:Función auxiliar que obtiene un conjunto con los distintos países, la cual a su vez, incorporaremos en las siguientes funciones 
* **<min_pais_por_edad_media>**:Función que incopora la función anterior(filtra_paises_por_media_edad) para calcular sobre el resultado de esta el país con menor tasa de edad media
* **<ordenar_paises_por_edad_media>**:Función que incopora la función anterior(filtra_paises_por_media_edad) para ordenar de mayor a menor los datos obtenidos de esta en función de la edad media
* **<agrupar_paises_por_ranking>**:Función que devuelve un diccionario cuyas claves son los países y los valores son los rankings que estos ocupan respecto al resto de países

### \<countries_population_test.py\>

* **<test_lee_fichero>**: La función recibe unos datos(en este caso, correspondientes a los países dados) obtenidos de la función 'lee_fichero' y se encarga de imprimir en pantalla las instrucciones dadas
* **<test_calcula_paises>**:Nos dice cúantos países distintos tiene el fichero de entrada 
* **<test_media_poblacion_cada_pais>**:La función recibe como parámetro los datos del fichero , sobre los cuales calcula la media(valor) de cada país(clave) en forma de diccionario 
* **<test_filtra_paises_por_media_edad>**: Recibe como parámetros de entrada los datos del fichero dado y un filtro en forma de número , el cual representa la edad media límite para construir el conjunto de salida, conformado por los países que cumplan dicho filtro
* **<test_min_pais_por_edad_media>**: Se encarga de filtrar el país con menor edad media, aprovechando los datos otorgados por la función anterior , en forma de tupla(País, edad media)
* **<test_ordenar_paises_por_edad_media>**:Se encarga de ordenar los países de mayor a menor , según su edad media, aprovechando los datos otorgados por la función anterior , en forma de un conjunto compuesto por tuplas(País, edad media)
* **<test_agrupar_paises_por_ranking>**:Recibe como parámetros de entrada los datos del fichero dado, con los cuales crea un diccionario en el cual las claves son los paises de dicho fichero y los valores , sus correspondientes rankings.

### \<modulo 2\>

* **<funcion 1>**: 
* **<funcion 2>**: 
* ...
