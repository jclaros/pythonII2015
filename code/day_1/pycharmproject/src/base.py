
"""
This is a comment
"""

'''
This is a comment too

Hola
'''


'''
mi_variable = "Hola Mundo!"
# imprimir el valor
print(mi_variable)
'''

# defincion de variables

variable = 1
m_variable = 2
v123_modulo = 1

#12variable =12

# boolean

boolean_variable = True

# Numbers, Listas, Booleanos, String, Diccionarion, Tuplas
print("-"*10)
print("Numbers")
print("-"*10)

print(" 7 + 2 = ", 7 + 2)
print(" 7 - 2 = ", 7 - 2)
print(" 7 * 2 = ", 7 * 2)
print(" 7 / 2 = ", 7 / 2)
print(" 7 % 2 = ", 7 % 2)
print(" 7 ** 2 = ", 7 ** 2)
print(" 7 // 2 = ", 7 // 2)

print("-"*10)
print("Strings")
print("-"*10)

nombre1 = "Rachel"
print("%s es %d %d alta" % (nombre1, 4, 5))
print("{} es {} {} alta".format(nombre1, 4, 5))




variable_string = "variable1"
print(variable_string)

variable_string2 = "variable2"
print(variable_string2)

variable_string3 = '\'variable 3 ' \
                    ' long ' \
                    ' really long string '
print(variable_string3)

variable_string4 = """
            ^^^^^^^^^^^^^^^^^^
            Este es un texto muy grande y
            con muchas lineas

            ps. demostrar que no existe diferencia real en el uso de comilla simple y doble
            ^^^^^^^^^^^
"""

print(variable_string4)



print("-"*10)
print("Listas")
print("-"*10)



compras = ['Mouse', 'Teclado', "Case", "Monitor"]

print(compras)

compras[0] = "Impresora"
#compras.append("Item fantasma")

#print(compras)

#compras.insert(1, "item entre elementos")

print(compras[1:3])


tareas = ["comprar las partes",
          "llevar las partes al lugar de ensamblado",
          "armar la computadora",
          "instalar SO"]

guia_global = [compras, tareas]
print(guia_global)

print(guia_global[0][2])
compras.append("Establizador")
tareas.append("instalar office")

print(guia_global)


print("-"*10)
print("Tuplas")
print("-"*10)


tupla = (1,2,3,4)
print(tupla)
print(tupla[0])
#tupla[0] = 9


lista = list(tupla)

lista[0] = 9
print(lista)

tupla = tuple(lista)
print(tupla)

print(len(tupla))
print(max(tupla))
print(min(tupla))


print("-"*10)
print("Diccionarios")
print("-"*10)

telefonos = {
    "jon": "8168731827987",
    "amed": "12838172638172",
    "mike": "12837618726",
    "jesse": "12534165243165"
}

print("El nro de telefono de Jon es: ", telefonos["jon"])

telefonos["michael"] = "217653716526"
telefonos["rachel"] = "9182739187293812"

print("El nro de telefono de Michael es: ", telefonos["michael"])

print(telefonos.keys())
print(telefonos.values())




print("-"*10)
print("Controles de flujo")
print("-"*10)

edad = 31


if edad > 25:
    print("hola señor")
elif edad > 20:
    print("Hola amigo")
else:
    print("Hola niño")

print("\n Iterate una lista de listas")




test_list = [[1,2,3], [10,20,30], [100, 200, 300]]

for index in range(0,3):
    print(index, test_list[index])

for i, v in enumerate(test_list):
    print(i, v)


for element in test_list:
    print(element)

print(test_list)

for i, v in enumerate(test_list):
    for index, value in enumerate(v):
        print(i, index, value)

print("-"*10)
print("While")
print("-"*10)
# while
import random

random_number = random.randrange(0,30)

while (random_number != 20):

    if random_number <= 8:
        print(" numero es menor a 9")
        break
    elif random_number % 7 == 0:
        print(" numero es modulo 7 ... cambiamos de numero")
        random_number = random.randrange(0,30)
        continue

    random_number = random.randrange(0,30)
    print(random_number)


print("-"*10)
print("Funciones")
print("-"*10)


def f(x, y):
    return x + y


print(f(9,5))


print("-"*10)
print("Switch")
print("-"*10)

def switch_function(x):
    return {
        'a': "primer caso",
        'b': "segundo caso"
    }.get(x, "caso por defecto")


print(switch_function("a"))
print(switch_function("m"))


print("-"*10)
print("Files")
print("-"*10)

archivo = open("test.txt", "wb")

print(archivo.name)
print(archivo.mode)

archivo.write(bytes("primera linea del archivo", "UTF-8"))

archivo.close()


archivo = open("test.txt", "r")
contenido = archivo.read()
print("contenido del archivo", contenido)

import os

os.remove("test.txt")









































































