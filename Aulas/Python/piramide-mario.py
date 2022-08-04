from cs50 import get_int

altura = get_int("Qual é a altura da pirâmide? ")

if altura > 0 and altura < 9:
    for i in range(altura):
        for j in range(i+1):
            print("# ", end="");
        print()


#Outra forma:
coluna = int(input("Número de colunas: "))
for i in range(coluna):
        for j in range(i+1):
            print("* ", end="");
        print("\n")