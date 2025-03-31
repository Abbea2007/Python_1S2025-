"""Escribe un programa que recorra una lista de cadenas y divida cada cadena 
en subcadenas utilizando un delimitador específico (por ejemplo, una coma 
o un espacio). """

list = []

def insertar_texto():
   cadena_lista = input("Ingrese la cadena de texto que desea separar con un separador: ")
   list.append(cadena_lista)

delimitador_espeficio = input("Ingrese el delimitador especifico: ")

def agregar_delimitador(lista):
   new_list = []
   for cadena in lista:
      convertida = cadena.split()
      new_list.append(convertida)
   return new_list 



insertar_texto()
resultado = agregar_delimitador(list)
print(f"La cadena separada con un delimitador especifico es: {resultado}")
while True:
    opcion = input("Desea ingresar otra cadena de texto: (s/n) => ").strip().lower()
    if opcion == "s":
       insertar_texto()
       resultado = agregar_delimitador(list)
       print(f"La cadena separada con un delimitador especifico es: {resultado}")
    elif opcion == "n":
       print("Gracias por usar")
       break
      




