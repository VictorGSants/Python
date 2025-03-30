pt = int(input("Digite o primeiro termo "))
r = int(input("Digite a razão "))
c = 1
count = 0
total = 0
x = 10
while x != 0:
    total = total + x
    while c <= total:
        print(pt, end=' ')
        c += 1
        pt += r
    print('pausa')
    x = int(input("Quantos termos vc quer mostrar a mais? "))
print(f"{total} termos mostrados")