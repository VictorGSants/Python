f = str(input('Digite sua frase ')).upper().replace(' ', '')
inversp = ''
for i in range(len(f) - 1, -1, -1):
    inversp += len(f[i])
    print(inversp)
    #nao consehui
