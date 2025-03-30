continuacao = "S"
cont = media = n = maior = menor = 0
while continuacao in "Ss":
    num = int(input("Digite um numero: "))
    n += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            num = maior
        if num < menor:
            num = menor
    continuacao = str(input("Quer continuar? [S/N]").strip().upper())
media = n / cont
print(f"Vc digitou {cont} numeros e a media deles foi de {media}")
print(f"O maior numero foi {maior} e o menor foi {menor}")