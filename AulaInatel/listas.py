notas = [] #lista vazia
soma = 0 #soma das notas

for i in range(0, 100): #estrutura de repetição até 100
    valor = int(input()) #valor da nota
    soma = soma + valor #atualizo a soma das notas
    notas.append(valor) #atualiza lista

media = soma / 100 #calcula a media com a soma atualizada
aprovados = 0 #variavel de contar os aprovados de 1 em 1
for i in range(0, 100):  #estrutura de repetição para verificar a lista
    if notas[i] >= media: #verificando a nota dos aprovadosa
        aprovados = aprovados + 1 #contando os aprovados de 1 em 1
        print(aprovados)

#pensativo