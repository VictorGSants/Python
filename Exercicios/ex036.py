print('-=-' * 15)
casa = float(input('Digite o valor da casa '))
salario = float(input('Digite seu salario '))
anos = float(input('Pretende pagar em quantos anos ? '))
print('-=-' * 15)
minino = salario * 30 / 100
meses = anos * 12
prestacao = (casa / meses)
print(f'A prestação ficou em {prestacao}')
if prestacao >= salario + minino:
    print('Não sera possivel realizar o emprestimo')
else:
    print(f'Será possivel efetuar o emprestimo  ')


