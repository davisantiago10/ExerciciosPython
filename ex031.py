km = int(input('Digite quantos Km sua viagem tem de distância:'))
p1 = km * 0.50
p2 = km * 0.45
if km <= 200:
    print('\033[36m Como sua viagem tem menos de 200km,\ncada km custará 50 centavos,')
    print('\033[36m Sua viagem tendo {} km, o preço que deverá ser pago é de R${:.2f}'.format(km, p1))
else:
    print('\033[33m Como sua viagem tem uma distância maior que 200km, \ncada km custará 45 centavos')
    print('\033[33m Sendo assim, sua viagem de {} km, custará R${:.2f}:'.format(km, p2))
