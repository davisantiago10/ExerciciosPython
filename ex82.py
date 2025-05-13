no = []
np = []
ni = []
while True:
    n = int(input('Digite um valor:'))
    no.append(n)
    if n % 2 == 0:
        np.append(n)
    elif n % 2 != 0:
        ni.append(n)
    opcao = str(input('Quer continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print('=-'*30)
print(f'Lista normal: {no}')
print(f'Lista dos pares: {np}')
print(f'Lista dos ímpares: {ni}')