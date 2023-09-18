v = float(input('Qual é a velocidade em que você está dirigindo: '))

p = (v - 80)*7

if v > 80:
    print('Você ultrapassou a velocidade máxima permitida de 80 km/h')
    print('Terá de pagar uma multa no valor de R${:.2f}'.format(p))
print('Tenha um ótimo dia e dirija com cuidado!')