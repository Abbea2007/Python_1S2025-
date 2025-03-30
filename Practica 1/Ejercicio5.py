"""Escribe un programa que recorra una lista de cadenas y reemplace todas 
las apariciones de un carácter específico con otro carácter, luego imprime la 
lista modificada."""

list = ["Hola mundo", "soy carlos abea", "estudio", "ingenieria en sistemas"]
print(list)

caracter_reemplazar = "o"
nuevo_caracter = "i"

def reempplazar(lista, viejo, nuevo):
    new_list = []
    for cadena in lista:
        resultado = cadena.replace(viejo, nuevo)
        new_list.append(resultado)
    return new_list

resultadocompleto = reempplazar(list, caracter_reemplazar, nuevo_caracter)

print(resultadocompleto)





