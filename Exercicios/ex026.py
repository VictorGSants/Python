frase = str(input('Digite uma frase ')).strip().lower()
fraseA = frase.strip().count('a')
print('Sua frase tem {} a'.format(fraseA))

posA = frase.find('a')
print('O primeiro aparaece na posição {}'.format(posA + 1))

posA2 = frase.rfind('a')
print('O ultimo a da frase aparece na posição {}'.format(posA2 +1))
