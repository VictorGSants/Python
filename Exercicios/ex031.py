distancia = float(input())
ate200 = distancia * 0.50
dps200 = distancia * 0.45
print(f'Voce pagara r$: {ate200 :.2f}' if distancia <= 200 else f'Voce pagara R$: {dps200 :.2f}'.upper())
