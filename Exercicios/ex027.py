nome = str(input('Digite seu nome completo')).strip()
n = nome.split()

nom2 = nome.lower()
print('Seu primeiro nome é {}'.format(nom2.split()[0]))

nom3 = nome.lower()
print('Seu ultimo nome é {}'.format(n[len(n)- 1] ))

