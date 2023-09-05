import math
cato = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
cata = float(input('Digite o valor do cateto adjacente do triângulo retângulo: '))
hip = math.sqrt(math.pow(cato,2)+math.pow(cata,2))
print('O valor da hipotenusa desse triângulo retângulo é {:.2f}'. format(hip))