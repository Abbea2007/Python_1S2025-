"""Escribe un programa que recorra una lista de cadenas y convierta cada 
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la 
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a 
minúsculas."""

list = ["Hola mundo", "soy carlos abea", "estudio", "ingenieria en sistemas"]
print(list)

def cadena_mayuminu(lista):
    new_list = []
    for cadena in lista:
        if len(cadena) % 2 == 0:
            resultado = cadena.upper()
        elif len(cadena) % 2 == 1:
            resultado = cadena.lower()
        new_list.append(resultado)
    return new_list

resultado_mayusmi = cadena_mayuminu(list)
print(f"La nueva lista es: {resultado_mayusmi}")

