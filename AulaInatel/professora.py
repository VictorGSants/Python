# Ler N e K
n, k = map(int, input().split())

# Criar lista de nomes
nome_alunos = []

# Estrutura de repetição para digitar os nomes na lista com o comando append
for i in range(n):
    nome = input()
    nome_alunos.append(nome)

# Colocar a lista em ordem alfabética com .sort()
nome_alunos.sort()

# Printar o aluno sorteado
aluno_sorteado = nome_alunos[k - 1]
print(aluno_sorteado)