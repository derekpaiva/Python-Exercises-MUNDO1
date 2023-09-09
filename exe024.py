city = str(input('Digite o nome de sua cidade: '))
city_div = city.split()

print('A cidade {} começa com o nome Santo?'.format(city), end=' ')
# o comando 'Santo' in city_div[0] procura na primeira palavra se tem Santo
print('Santo' in city_div[0])