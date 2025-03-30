x = float(input()) #introduzi o valor de x e y
y = float(input())

if x > 0 and y > 0:     #condiçoes
    print('Q1')

elif x < 0 and y > 0:
    print('Q2')

elif x < 0 and y < 0:
    print('Q3')

elif x == 0 or y == 0:
    print('Eixos')

else: print('Q4')

#facil