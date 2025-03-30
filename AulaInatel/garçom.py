n = int(input())
c = 0
lista = []

for i in range(n):
    l, c = map(int, input().split())
    lista.append(l and c)
    if l > c:
        x = 0 + c
       print(c)
