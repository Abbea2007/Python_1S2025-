"""Escribe un programa que recorra una lista de cadenas y cuente cuántas 
veces aparece un carácter específico en cada cadena. Al final, muestra el 
conteo para cada cadena."""

list_cadenas = ["Holo", "mo llomo", "carlos", "estudio ingenieria en sistemas"]
print(list_cadenas)

caracter_contar = "o"

def contar_caracter(lista, caracter):
    new_list = []
    for cadena in lista:
        conteo = cadena.count(caracter)
        new_list.append(conteo)
    return new_list

resultado = contar_caracter(list_cadenas, caracter_contar)

print(f"La cantidad de veces que aparece {caracter_contar} en cada cadena es: {resultado}")
