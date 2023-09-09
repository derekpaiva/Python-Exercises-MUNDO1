#esse programa é em formato de string
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
# o operador // pega o a parte inteira do quocioente
# o operador % pega o resto da divisão
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}...'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))