""""
nome = str(input('Qual é seu nome? ')).title()
if nome == 'Victor':
    print('Que nome lindo! ')
else:
    print('Que nome feio vc tem')
print('Bom dia, {}'.format(nome))

"""

#modo simplificado :
n1 = float(input("nota 1: "))
n2 = float(input('nota 2: '))
m = (n1+n2)/2
print("Sua media foi {:.1f}".format(m))

print('PARABENS' if m >= 6 else 'Burro')

#modo Comum: 
""""
if m >= 6.0:
    print('Parabens!! Sua media foi boa')
else:
    print('Sua media foi abaixo do esperado! Estude mais !')
"""