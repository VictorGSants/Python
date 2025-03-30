print('-=-' * 10)
somaidade = 0
mediaidade = 0
cont = 0
for c in range(4):
    n = str(input('Digite o nome da pessoa: '))
    i = int(input('Digite a idade da pessoa: '))
    s = str(input('Digite o sexo da pessoa M/F: ').upper())
    somaidade += 1
    print('-=-' * 10)
    if s == 'F' and i < 20:
        cont = cont + 1
mediaidade = somaidade / 4
print(f'A media das idades foram {mediaidade}')
print(f'As mulheres que tem menos de 20 anos sao: {cont}')
