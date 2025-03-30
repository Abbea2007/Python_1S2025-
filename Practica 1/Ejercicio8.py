"""Escribe un programa que recorra una lista de cadenas y las ordene 
alfabéticamente en orden ascendente. """

list_cadenas = ["Hola", "llamo", "Carlos", "estudios"]
print(list_cadenas) 

def ordenar_lista(lista):
    return sorted(lista)  

resultado = ordenar_lista(list_cadenas)

print("Lista ordenada:", resultado)