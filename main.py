import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sa = int(input('Cuantos digitos debe tener su password? '))

x = ''

for i in range(sa):
    x += random.choice(caracteres) 

print(x)
