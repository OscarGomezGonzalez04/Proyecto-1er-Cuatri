from datetime import datetime

def parsea_fecha(cadena):
    result = datetime.today().date()
    if cadena != '':
        result = datetime.strptime(cadena, '%d/%m/%Y' ).date()
    return result

def parsea_boolean(cadena):
    mayusculas = cadena.upper()
    return mayusculas == 'TRUE'