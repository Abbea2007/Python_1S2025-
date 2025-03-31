"""Escribe un programa que recorra una lista de cadenas y convierta cada 
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la 
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a 
minúsculas."""

list = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ").strip()
    cadene_separada = cadena.split(",")
    list.extend(cadene_separada)

def convertir_cadena(lista):
    for string in lista:
        if len(string) % 2 == 0:
         print(string.upper())
        elif len(string) % 2 == 1:
         print(string.lower())     
    
pedir_cadena()
conversion = convertir_cadena(list)


while True:
    list.clear()
    option = input("¿Deseas convertir otra cadena? (s/n) => ").strip().lower()
    if option == "s":
        pedir_cadena()
        conversion = convertir_cadena(list)
    elif option == "n":
        print("Gracias por usar")
        break





