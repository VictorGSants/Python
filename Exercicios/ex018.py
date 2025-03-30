from math import radians
from math import sin
from math import cos
from math import tan


num = float(input((print('Insira o numero'))))
seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))
print('o seno desse numero é {:.2f}\no cosseno é {:.2f}\na tangente é  {:.2f}'.format(seno, cosseno, tangente))

