from math import hypot
x = float(input(print('Insira o valor do cateto adjacente')))
y = float(input((print('insira o valor do cateto oposto'))))
hipotenusa = hypot(y, x)
print("O valor da Hipotenusa vale {:.2f}".format(hipotenusa))