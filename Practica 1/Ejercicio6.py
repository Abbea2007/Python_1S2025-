"""Escribe un programa que recorra una lista de cadenas y elimine los 
espacios en blanco al principio y al final de cada cadena."""

list_cadenas = [" Hola ", " me llamo ", " carlos ", " estudio ingenieria en sistemas "]
print(list_cadenas)

def eliminar_espacio(lista):
    new_list = []
    for cadena in lista:
        eliminado = cadena.strip()
        new_list.append(eliminado)
    return new_list

resultado = eliminar_espacio(list_cadenas)

print(f"La cadenena sin espacios es: {resultado}")