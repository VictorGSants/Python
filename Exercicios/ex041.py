from time import sleep
from datetime import date
#
print('-=-'*20)
#
anoN = int(input('Qual o ano de nascimento do(a) atleta ? '))
ano = date.today().year
idade = ano - anoN
#
print('-=-'*20)
#
print('CALCULANDO......')
sleep(3)
print(f'O(A) atleta tem {idade} anos')
#
print('-=-'*20)
if idade < 9:
    print('Categoria: Mirim')
elif idade < 14:
    print('Categoria: Infantil')
elif idade < 19:
    print('Categoria: Junior ')
elif idade <= 20:
    print('Categoria: Sênior ')
else: print('Categoria: Master')




