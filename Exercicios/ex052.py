tot = 0
num = int(input('Digite um numero: '))
for i in range(1, num + 1):
    if num % i == 0:
        tot += 1
print(f'O numero {num} foi divisivel {tot} vezes ')
if tot == 2:
    print(f"o numero {num} é primo ")
else:
    print('O numero nao é primo')