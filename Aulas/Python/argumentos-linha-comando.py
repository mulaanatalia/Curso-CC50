#DEVE-SE PASSAR UM ARGUMENTO DE LINHA DE COMANDO
from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")

#Fazer com que o python itere sobre a lista
from sys import argv

for arg in argv:
   print(arg)