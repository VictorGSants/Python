r1 = float(input('Digite um lado do triangulo '))
r2 = float(input('Digite outro lado do triangulo '))
r3 = float(input('Digite outro lado do triangulo '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print('Seu triangulo é equilatero ')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Seu triangulo é isoceles ')
    else:
        print('Seu triangulo é escaleno ')
else:
    print('Não pode se formar um triangulo com esses valores')