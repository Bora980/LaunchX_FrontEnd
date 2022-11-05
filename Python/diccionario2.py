'''
Diccionario2
Autor: Txus
'''

# Declaracion de variables globales

continuar = True
productos = [] # Lista para contener los diferentes productos


# Imprime Tútilo
# Muestra por pantalla el texto que se le pasa por parámetro
# param string cadena


def imprime_titulo(cadena):
    print(f"- {cadena.upper():10} -------------------")

def nuevo_producto():
    # Crear el tipo diccionario de producto
    producto = dict()
    # Pregunto los valores
    producto['descripcion'] = pregunta("Descripción -> ")
    producto['familia'] = pregunta("Familia -> ")
    producto['precio'] = pregunta("Precio -> ")

    # Añadirlo a la lista
    global productos #Hace referencia a utilizar la variable global
    productos.append(producto)

# Pregunta
# Mestra por consola la pregunta que le paso por parámetro
# param string texto_progunta
# return string

def pregunta(texto_pregunta):
    return input(f"{texto_pregunta} :")

# Imprime Tabal
# Muestra por pantalla el contenido de la lista de productos y la cabecera
def imprime_tabla():
    #imprime cabeceras
    imprime_linea_tabla("Descripción", "Familia", "Precio")
    imprime_linea_tabla("-------------", "-------------", "-------------")
    # recorre la lista para imprimer los productos
    for producto in productos:
        imprime_linea_tabla(producto['descripcion'],producto['familia'],producto['precio'])
    imprime_linea_tabla("-------------", "-------------", "-------------")


# Imprime Línea Tabla
# Imprime una única línea de la tabla
# param string descripcion
# param string familia
# param string precio

def imprime_linea_tabla(descripcion, familia, precio):
    print(f"{descripcion:30} {familia:15} {precio:5}")

# Inicio
imprime_titulo("inicio")

#Bucle infinito para introfucir nuevos productos

while continuar:
    #Pregunta inicial
    print("Indica FIN para finalizar")
    print("Pusla intro para nuevo producto")
    respuesta= pregunta(" ->")
    if respuesta.upper() == "FIN":
        break
    else:
        #se no sale, pregunta nuevo producto
        nuevo_producto()

print(productos)

imprime_tabla()
#for v in productos:
#    descripcion, familia, precio = v
#   print("{:<8} {:<15} {:<10}".format(descripcion, familia, precio))

imprime_titulo("fin")