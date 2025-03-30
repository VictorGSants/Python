from datetime import date
contMenor = 0
contM = 0
v = 0
hj = date.today().year


for i in range(1, 8):
    v = v + 1
    anos = int(input(print(f'Digite o ano de nascimento da {v}° pessoa: ')))
    if hj - anos >= 18:
        contM = contM + 1
    else:
        contMenor = contMenor + 1

print(f'Das 7 pessoas, {contM} são maiores de idade. ')
print(f'Das 7 pessoas, {contMenor} são menores de idade. ')


