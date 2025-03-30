n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite um numero [999 para parar]: "))
    soma = soma + n
    cont += 1
print(f"A soma dos numeros é {soma - 999}")
print(f"Voce digitou {cont - 1} numeros")
print("FIM")
