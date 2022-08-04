#Implementadndo pesquisa linear verificando cada elemento em uma lista
import sys

numbers = [4, 6, 8, 2, 7, 5, 0]

if 1 in numbers:
    print("Encontrado")
    sys.exit(0)

print("Nao Encontrado")
#sys.exit(1)

#Pesquisando numa lista de strings
names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

if "Ron" in names:
    print("Found")
else:
    print("Not found")

#consulta no dicionário
from cs50 import get_string

people = {
"Brian": "+1-617-495-1000",
"David": "+1-949-468-2750"
}

name = get_string("Nome: ")
if name in people:
    print(f"Numero: {people[name]}")