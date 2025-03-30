"""Escribe un programa que busque si una sub cadena está presente en cada 
una de las cadenas de una lista. El programa debe devolver una lista con 
valores booleanos que indiquen si la sub cadena fue encontrada en cada 
cadena."""

list = ["Hola mundo", "soy carlos abea mundo", "estudio mundo", "ingenieria en sistemas"]
print(list)

sub_cadena = "mundo"

def find_subcadena(lista, subcadena):
    new_list = []
    for cadena in lista:
        new_list.append(subcadena in cadena)
    return new_list

resultado = find_subcadena(list, sub_cadena)

print(resultado)
