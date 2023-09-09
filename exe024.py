city = str(input('Digite o nome de sua cidade: ')).strip()
city2 = city.title()
city_div = city2.split()

print('A cidade {} começa com o nome Santo?'.format(city2), end=' ')
# o comando 'Santo' in city_div[0] procura na primeira palavra se tem Santo
print('Santo' in city_div[0])