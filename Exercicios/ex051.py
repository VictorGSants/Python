from time import sleep

primeiroTermo = int(input('Digite o primeiro termo da PA '))
r = int(input('Digite a razão da PA '))
print(f'OS 10 primeiros termos dessa PA são: ')
print('CARCULANDO ................................')
sleep(2)
print(primeiroTermo)
for i in range(10):
    primeiroTermo += r
    print(primeiroTermo)