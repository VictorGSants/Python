n = int(input('Digite um numero: '))
d = int(input(print(f"""Seu numero é {n}, Caso queira converte-lo, digite:
[ 1 ]- Binario 
[ 2 ] - octal
[ 3 ] - hexadecimal""")))

binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)

if d == 1:
    print(f'A conversão de {n} para binario sera: {binario}')
elif d == 2:
    print(f'A converção de {n} para octal sera : {octal}')
elif d == 3:
    print(f'A conversão de {n} para hexadecimal é {hexadecimal}')

