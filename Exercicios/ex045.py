from time import sleep
from random import randint
print('VAMOS JOGAR JOKEMPO !')
eu = str(input('Pedra, Papel ou tesoura? '.lower()))
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')

x = randint(1, 3)
if x == 1:
    print('Eu escolhi pedra ')
    if eu == 'pedra':
        print('Empatamos !')
    elif eu == 'papel':

        print('Droga, voce ganhou !')
    elif eu == 'tesoura':
        print('Eu ganhei ! HAHAHAHA ')

elif x == 2:
    print('Eu escolhi papel ')
    if eu == 'papel':
        print('Empatamos !')
    elif eu == 'tesoura':
        print('Droga, voce ganhou !')
    elif eu == 'pedra':
        print('Eu ganhei ! HAHAHAHA ')
elif x == 3:
    print('Eu escolhi tesoura ')

    if eu == 'pedra':
        print('Droga, voce ganhou')
    elif eu == 'papel':
        print('Eu ganhei, HAHAHAHA !')
    elif eu == 'tesoura':
        print('Empatamos !')
