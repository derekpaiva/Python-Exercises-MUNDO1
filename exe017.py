import math
cato = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
cata = float(input('Digite o valor do cateto adjacente do triângulo retângulo: '))
print('O valor da hipotenusa desse triângulo retângulo é {:.2f}'. format(math.hypot(cato, cata)))