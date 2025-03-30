c = 0 # contadoror
v = 0
for i in range(0, 500): # esrutura de rep
    if i % 2 != 0 and i % 3 == 0: # condição
        c += i
        v += 1
        print(i)
print(f'A soma destes numero é {c}')
print(f'Existem {v} valores ')
