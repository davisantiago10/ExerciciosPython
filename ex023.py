num = int(input('Escreva um número que esteja entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 %10
print('-' * 5,'\033[33m Assim fica a distribuição desse número', '\033[m-' * 5)
print('\033[36m Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))




