import datetime
from time import sleep
data = datetime.date.today()
print(f'Seu sistema corre no dia de {data}')
n1 = float(input('Digite sua nota 1 '))
n2 = float(input('Digite sua nota 2 '))
media = (n1 + n2) / 2
print('PROCESSANDO...........')
sleep(3)
print(f'Sua media foi {media}')
if media < 5.0:
    print('reProvadO'.upper())
elif media <= 6.9:
    print('recuperação'.upper())
else:
    print('aprovado ! boas ferias '.upper())
