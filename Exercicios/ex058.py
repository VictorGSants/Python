from random import randint
from time import sleep
print("Vou pensar em um numero de 0 a 10, tente adivinhar...")
sleep(3)

cont = 0
num = randint(0, 10)
s = int(input('Digite o numero que vc acha '))
while s != num:
    if num > s:
        s = int(input("Mais, tente novamente "))
    elif num < s:
        s = int(input('Menos, tente novamente '))

    cont += 1
if s == num:
    print(f'Voce acertou, eu estava pensando no numero {num}')
print(f'Voce errou {cont} vezes')

