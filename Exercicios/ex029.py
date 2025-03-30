velocidade = float(input())
multa = (velocidade - 80) * 7

print(f'Voce foi multado em R$: {multa :.2f} REAIS'.upper() if velocidade > 80 else 'Sua velocidade esta ok')

"""""
if velocidade > 80:
    print(f'Voce foi multado em R$: {multa :.2f}')
else:
    print('Sua velocidade esta ok')
"""""
