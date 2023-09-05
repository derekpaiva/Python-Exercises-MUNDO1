import math
from math import pow, sqrt

cato = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
cata = float(input('Digite o valor do cateto adjacente do triângulo retângulo: '))
h = cato**2 + cata**2
hip = math.sqrt(h)
print('O valor da hipotenusa desse triângulo retângulo é {:.2f}'. format(hip))