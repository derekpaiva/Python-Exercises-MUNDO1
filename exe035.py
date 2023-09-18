a = float(input('Digite o valor do tamanho do primeiro segmento: '))
b = float(input('Digite o valor do tamanho do segundo segmento: '))
c = float(input('Digite o valor do tamanho do terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos informados podem formar um triângulo.'.format(a, b, c))
else:
    print('Os segmentos informados não podem formar um triângulo.')