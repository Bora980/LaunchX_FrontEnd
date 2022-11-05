'''
variable y funciones
Autor: Txus
'''

# Declaracion de variables globales
nombre = "Txus"
numero = 10
contador = 1

# Decclaracion de funciones

# Imprime Tútilo
# Muestra por pantalla el texto que se le pasa por parámetro
# param string cadena

#def pregunta_nombre():
#    return input("Dime tu nombre :")

#def pregunta_numero():
#    return input("Dime un número :")

# Pregunta
# Mestra por consola la pregunta que le paso por parámetro
# param string texto_progunta
# return string

def pregunta(texto_pregunta):
    return input(f"{texto_pregunta} :")

def imprime_titulo(cadena):
    print(f"- {cadena.upper():10} -------------------")

# Inicio
imprime_titulo("inicio")
nombre = pregunta("Dime tu nombre")
numero = int(pregunta("Dime tu número"))

imprime_titulo("Bucle WHILE")
while contador <= numero:
    print(f" {contador} - {nombre} es el número {numero} ")
    contador += 1 #contador = contador + 1

# Bucle FOR
imprime_titulo("Bucle FOR")
for i in range(0, numero + 1):
    print(f" {i} {numero} es el número {numero}")

imprime_titulo("fin")