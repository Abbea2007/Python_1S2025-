"""Crea una lista de cadenas de texto. Escribe un programa que recorra esta 
lista y concatene todas las cadenas en una sola cadena, separadas por un 
espacio."""
"""""
list = ["Hola mundo", "soy carlos abea", "estudio", "ingenieria en sistemas"]
print(list)

for cadena in list:
    separar = " ".join(list)

print(f"La lista concatenada es: {separar}")

"""""

listl = list()

def add_string_text():
  listl.append(input("Inserte la cadena de texto => "))

caracter_delimitador = " "
def convert_to_substrings(list_of_strings, caracter):
  new_list = []
  for string in list_of_strings:
   sub_string = string.split(caracter)
   new_list.extend(sub_string)
   return new_list


while True:
  if input(("Desea agregar una cadena de texto ('n' para salir) => ")).lower() != "n":
    add_string_text()
    modified_list = convert_to_substrings(listl, caracter_delimitador)
    print(modified_list)
    continue
    print("Gracias por usar")
    break   