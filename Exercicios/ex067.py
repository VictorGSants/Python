while True:
    t = int(input("Quer ver a tabudada de que valor? "))
    if t < 0:
        break
    print(f"""{t} x 01 = {t}
{t} x 02 = {t * 2}
{t} x 03 = {t * 3}
{t} x 04 = {t * 4}
{t} x 05 = {t * 5}
{t} x 06 = {t * 6}
{t} x 07 = {t * 7}
{t} x 08 = {t * 8}
{t} x 09 = {t * 9}
{t} x 10 = {t * 10}""" )

print("Programa encerrado, volte sempre")
