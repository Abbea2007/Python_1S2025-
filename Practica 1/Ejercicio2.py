""" Escribe un programa que recorra una lista de cadenas y calcule la longitud 
de cada cadena, almacenando el resultado en una nueva lista. """

list = []

def pedir_cadena():
    cadenas = input("Ingrese la cadena: ")
    subcadenas = cadenas.split(",")
    list.extend(subcadenas)  



def calcular_longitud(lista):
    new_list = []
    for cadena in lista:
        longitud = len(str(cadena))
        new_list.append(longitud)
    return new_list

pedir_cadena()
resultado = calcular_longitud(list)
print(f"Las longitudes de las cadenas son: {resultado}")
while True:
    list.clear()
    option = input("¿Te gustaría ingresar otra cadena? (s/n) => ").strip().lower()
    if option == "s":
        pedir_cadena()
        resultado = calcular_longitud(list)
        print(f"Las longitudes de las cadenas son: {resultado}")
    elif option == "n":
        print("Gracias por usar")
        break
    