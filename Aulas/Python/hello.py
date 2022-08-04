#print("ola, mundo")
#entrada do teclado usando input:
resposta = input("Seu nome: ")
print(f"Ola, {resposta}")

from cs50 import get_string

resposta = get_string("Qual é o seu nome? ")

#print("Olá, " + resposta) outra forma de concatenar uma variavel:
print(f"Ola, {resposta}")