import csv

from cs50 import get_string

file = open("phonebook.csv", "a")

name = get_string("Nome: ")
number = get_string("Numero: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()