'''
variable y funciones
Autor: Txus
'''

# Declaracion de variables globales
lista = ["Perro", "gato", "peces"]
continuar = True

# Decclaracion de funciones

# Imprime Tútilo
# Muestra por pantalla el texto que se le pasa por parámetro
# param string cadena


def imprime_titulo(cadena):
    print(f"- {cadena.upper():10} -------------------")

# Imprime Lista
# Muestra por pantalla cada elemento de la lista

def imprime_lista():
    # lista.clear() es para limpiar lista
    for mascota in lista:
        print(mascota)
   # else: #else tambien lo lleva for si en el caso de que la lista esté vacia
   #     print("El listado está vacio")

    print(f"- El listado contiene {len(lista)} elementos")

# Inicio
imprime_titulo("inicio")

# Pregunta
# Mestra por consola la pregunta que le paso por parámetro
# param string texto_progunta
# return string

def pregunta(texto_pregunta):
    return input(f"{texto_pregunta} :")

lista.insert(1,"hamster") # inserta el elemento en la posición deseada

while continuar:
    print("Indica Fin para Finalizar")
    print("Indica BORRAR para limpiar el listado")
    print("Indica ORDENAR para ordenar la lista")
    print("Dime una mascota")

    respuesta = pregunta(" -> ")
    if respuesta.upper() == "FIN":
        break
    elif respuesta.upper()== "BORRAR":
        lista.clear()
        print(f"- El listado contiene {len(lista)} elementos")
    elif respuesta.upper()== "ORDENAR":
        lista.sort()
        imprime_lista()
    else:
        lista.append(respuesta) #append es para meter elementos a la lista

imprime_lista()
imprime_titulo("fin")