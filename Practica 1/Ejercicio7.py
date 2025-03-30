"""Escribe un programa que recorra una lista de cadenas y divida cada cadena 
en subcadenas utilizando un delimitador específico (por ejemplo, una coma 
o un espacio). """

list_cadenas = ["Hola mundo", "me llamo Carlos", "estudio ingeniería"]
print(list_cadenas)

delimitador_especifico = " "

def dividir_cadena(lista, caracter):
    new_list = []
    for cadena in lista: 
        resultado = cadena.split(caracter) 
        new_list.append(resultado)
    return new_list

result = dividir_cadena(list_cadenas, delimitador_especifico)

print(f"La cadena dividida por un delimitador especifico es: {result}")
