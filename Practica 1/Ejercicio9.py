"""Escribe un programa que recorra una lista de cadenas y elimine aquellas 
que estén vacías. Imprime la lista resultante."""

list_cadenas = ["Hola", "me llamo", "  ", "carlos", "                        ", "estudio ingenieria en sistemas"]
print(list_cadenas)

def delate_cadenull(lista):
    newlist = []
    for cadena in lista:
        if cadena.strip() != "":
            newlist.append(cadena)
    return newlist

resultado = delate_cadenull(list_cadenas)

print(f"La lista sin espacios es: {resultado}")
            
        
        

