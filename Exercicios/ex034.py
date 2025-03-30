salario = float(input())
aumento = (salario / 100) * 10
aumento2 = (salario / 100) * 15
print(aumento)
if salario > 1250:
    print(f'O seu aumento sera de 10% e seu novo salario é de r$: {salario + aumento :.2f}'.title())
else:
    print(f'O seu aumento sera de 15% e seu novo salario é de r$:  {salario + aumento2 :.2f}'.title())
