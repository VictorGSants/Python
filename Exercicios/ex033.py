n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 > n3:
    print(f'o maior numero é {n1}')
elif n2 > n1 > n3:
    print(f'o maior numero é {n2}')
else:
    print(f'o maior numero é {n3}')


if n1 < n2 < n3:
    print(f'O menor numero é {n1}')
elif n2 < n3 < n1:
    print(f'O menor numero é {n2}')
else:
    print(f'o menor numero é {n3}')
    
