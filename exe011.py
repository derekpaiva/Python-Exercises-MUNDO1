l = float(input('Digite o valor da largura da parede, em metros: '))
a = float(input('Agora digite o valor da altura, em mtros: '))
area = l*a
tinta = area/2
print('A área da parede é {:.2f} m2 \n E precisará de {:.2f} litros de tinta'.format(area, tinta))