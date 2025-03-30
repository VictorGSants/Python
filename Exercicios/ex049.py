from time import sleep
print('-=-' * 10)
num = int(input('Digite o numero da sua tabuada: '))
print('CARCULANDO.......')
c = 0
sleep(2)
for i in range(10):
    c = c + 1
    print(f'{num:2} X {c :2} = {num * c}')
