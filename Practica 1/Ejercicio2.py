""" Escribe un programa que recorra una lista de cadenas y calcule la longitud 
de cada cadena, almacenando el resultado en una nueva lista. """

list = ["Hola mundo", "soy carlos abea", "estudio", "ingenieria en sistemas"]
print(list)

def calcular_longitud(lista):
    new_list = []
    for cadena in lista:
        conteo = len(str(cadena))
        new_list.append(conteo)
    return new_list

resultado = calcular_longitud(list)

print(f"La longitud de cada cadena es: {resultado}")
    