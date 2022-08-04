scores = [72, 73, 33]

print("Média: " + str(sum(scores) / len(scores)))

#Com string formatada
print(f"Média formatada: {sum(scores) / len(scores)}")

#Adicionar itens a lista
from cs50 import get_int

scores = []
for i in range(3):
    scores.append(get_int("Score: "))

for i in range(3):
    print(scores[i])

#Iterar sobre cada caractere em uma string
from cs50 import get_string

s = get_string("Antes: ")
print("Depois: ", end="")

for c in s:
    print(c.upper(), end="")
    print()