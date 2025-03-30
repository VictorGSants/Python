c = 0
for i in range(6):
    x = int(input('Digite um numero: '))
    if x % 2 == 0:
        c += x

print(f'A soma dos numeros pares é {c}')
