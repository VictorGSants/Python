from random import shuffle
n1 = str(input(print('Digite o nome do primeiro aluno ')))
n2 = str(input(print('Insira o nome do segundo aluno ')))
n3 = str(input(print('insira o nome do terceiro aluno ')))
n4 = str(input((print('Insira o nome do terceiro aluno '))))

ordem = [n1, n2, n3, n4]

shuffle(ordem)
print(ordem)
