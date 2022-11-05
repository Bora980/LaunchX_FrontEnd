'''
Fechas
Autor: Txus
'''
# Importación de librerías
#import datetime # importar todo de esta librería
#from datetime import datetime # importa solo ese módulo de la librería y no todo de ella
import fechas2

# Declaracion de variables globales

hoy = ""

# Imprime Tútilo
# Muestra por pantalla el texto que se le pasa por parámetro
# param string cadena


def imprime_titulo(cadena):
    print(f"- {cadena.upper():10} -------------------")


imprime_titulo("inicio")

#hoy = fechas2.dame_fecha_hoy()
dia= input('Dime el dia: ')
mes = input('Dime el mes: ')
anyo = input('Dime el anyo: ')
hoy=fechas2.convierte_a_fecha(dia,mes,anyo)

#print(fechas2.pon_formato(hoy))
#print(fechas2.dame_fecha_larga(hoy))

#dias = int(input("Dime el número de días a incrementar:: "))
#nueva_fecha = fechas2.incrementa_dias(hoy,dias)
#print(fechas2.pon_formato(nueva_fecha))

imprime_titulo("fin")