from random import randint
from time import sleep

print('-=-' * 20)
print('adivinhe o valor que eu estou pensando (de 0 a 5) '.upper())
print('-=-' * 20)

n = int(randint(0, 5))
s = int(input())
print('PROCESSANDO ...')
sleep(3)

if s == n:
    print('parabens!! voce ganhou.'.upper())
    print('eu estava pensando no numero '.format(n))
else:
    print('voce errou!!'.upper())
    print('o numero era {}'.format(n))
