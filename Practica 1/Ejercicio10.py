"""Escribe un programa que recorra una lista de cadenas y cuente cuántas 
veces aparece un carácter específico en cada cadena. Al final, muestra el 
conteo para cada cadena."""

list = []

def pedir_cadena():
    cadena = input("Ingrese la cadena para contar los caracteres: ")
    cadena_separada = cadena.split(",")
    list.extend(cadena_separada)

caracter_especifico = "o"

def contar_caracteres(lista, caracter):
    new_list = []
    for string in lista:
        result = string.count(caracter)
        new_list.append(result)
    return new_list

pedir_cadena()
resultado = contar_caracteres(list, caracter_especifico)
print(resultado)

while True:
    list.clear()
    option = input("Desea ingresa otra cadena: (s/n = >)").lower()
    if option == "s":
        pedir_cadena()
        resultado = contar_caracteres(list, caracter_especifico)
        print(resultado)
    elif option == "n":
        print("Nos vemos")
        break




