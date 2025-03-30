from random import choice

n1 = str(input(print('Digite o nome do aluno 1 ')))
n2 = str(input(print('Digite o nome do aluno 2 ')))
n3 = str(input(print('Digite o nome do aluno 3 ')))
n4 = str(input(print('Digite o nome do aluno 4 ')))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))