import math

a = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print('O ângulo {:.2f}º possui \n sen {:.2f}º = {:.2f} \n cos {:.2f}º = {:.2f} \n tg {:.2f}º = {:.2f}'.format(a, a, sen, a, cos, a, tg))