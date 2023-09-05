km = int(input('Informe a quantidade de quilômetros rodados pelo carro: '))
d = int(input('Agora, informe a quantidade de dias que ficou com o carro: '))
pagar = 0.15*km + 60*d
print('O valor a ser pago, em reais, por {} km rodados em {} dias é de R$ {}.'.format(km, d, pagar))