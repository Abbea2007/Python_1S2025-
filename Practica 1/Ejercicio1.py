"""Crea una lista de cadenas de texto. Escribe un programa que recorra esta 
lista y concatene todas las cadenas en una sola cadena, separadas por un 
espacio."""

list = ["Hola mundo", "soy carlos abea", "estudio", "ingenieria en sistemas"]
print(list)

for cadena in list:
    separar = " ".join(list)

print(f"La lista concatenada es: {separar}")



