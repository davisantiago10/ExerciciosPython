#Código que calcula a medida da hipotenusa
from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Diga o valor do cateto adjacente:'))
hip = hypot(ca, co)
print('A medida da hipotenusa é: {:.2f}'.format(hip))

