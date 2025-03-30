print('=' * 12)
nome = str(input(print('Insira seu nome completo')))
nome1 = nome.upper()
print('Seu nome em maiuscula sera {}'.format(nome1))

nome2 = nome.lower()
print('Seu nome em minusculo sera {}'.format(nome2))

nome3 = len(nome.replace(' ', ''))
print('Seu nome sem espaços tera {}, letras sem contar os espaços'.format(nome3))

nome4 = nome.split()[0]
print('Seu primeiro nome é {}'.format(nome4))