x = 2
y = 3

from cs50 import get_int, get_string

x = get_int("x: ")
y = get_int("Y: ")

if x < y:
    print("X é menor que Y")
elif x > y:
    print("X é maior que Y")
else:
    print("X é igual a Y")


#Comparação de strings
s = get_string("Você concorda?")

if s == "Y" or s == "y":
    print("Concordo")
elif s == "N" or s == "n" :
    print("Não concordo.")