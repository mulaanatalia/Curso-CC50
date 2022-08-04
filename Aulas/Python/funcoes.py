def main():

    for i in range(3):
        miau()

def miau():
    print("miau")

main()

#Função com input
def main():
    miau(3)
def miau(n):
    for i in range(n):
        print("CERTO")

main()

from cs50 import get_int

def main():
    i = get_positive_int()
    print(i)

def get_positive_int():
    while True:
        n = get_int("Inteiro Positivo: ")
        if n > 0:
            break
        return n

main()