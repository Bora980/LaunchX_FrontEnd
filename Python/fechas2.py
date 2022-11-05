'''
Librería de funciones de fechas
Autor: Txus
'''

# dame_fecha_hoy() -> Devuelve la fecha del día
# pon_formato(fecha) -> Devuelvía un str con la fecha en formato DD/MM/AA
# dame_fecha_larga(fecha) -> Devuelve un str con la fecha en formato DD de MMMM de AAAA
# incrementa_dias(fecha,dias) -> Devuelve una fecha tras incrementar a la fecha dada los días


# Importación de librerías
#import datetime # importar todo de esta librería
from datetime import datetime # importa solo ese módulo de la librería y no todo de ella
from datetime import timedelta 

# Declaración de variables globalaes

meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

# Dame fecha hoy
# Devuelve la fecha y hora del system
# return datetime

def dame_fecha_hoy():
    return datetime.now()

# Pon Formato
# Cambioa el formato de la fecha a DD/MM/AA
# param daterime fecha
# return string

def pon_formato(fecha):
    return fecha.strftime('%d/%m/%Y %H:%I:%S')

# Dame Fecha Larga 
# Devuelve la fecha que recibe como parámetro con un formato dado
# param datatime fecha
# return string

def dame_fecha_larga(fecha):
    return f"{fecha.day} de {meses[fecha.month-1]} de {fecha.year}"

# Incrementa Dias
# Suma a la fecha pasada por parámetro, el número de días indicado
# param datetime fecha
# param int
# return datatime

def incrementa_dias(fecha, dias):
    return fecha + timedelta(days=dias)

# Convierte A Fecha
# Convierte una cadena en una fecha
# param str dia
# param str mes
# param str anyo
# return datetime

def convierte_a_fecha(dia,mes,anyo):
    print(f"{anyo}/{mes}/{dia}")
    #return datetime(f"{anyo}/{mes}/{dia}")