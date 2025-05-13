numero = int(input('Fatorial de: '))
cont = numero
f = 1
print('Calculando {}! : '.format(numero), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))



