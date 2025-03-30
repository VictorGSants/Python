from math import factorial
x = int(input("Digite um numero para calcular o fatorial: "))
# print(factorial(x))
c = 1
f = 2
print(f"Calculando {x}!...")
while f <= x:
    c = c * f
    f = f + 1
    print(c)
