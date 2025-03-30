print("FIBONACCI")
print("-=-"*10)
n = int(input("Quantas sequencias vc quer? "))
print("-=-"*10)
t1 = 0
t2 = 1
cont = 0
print(f"{t1} -> {t2}",end='')
while cont < n + 1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont +=1
    print(f" -> {t3}", end='')