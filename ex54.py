tot_menor = 0
tot_maior = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 21:
        tot_maior += 1
    elif idade < 21:
        tot_menor += 1

print('Há {} pessoas que são maiores de idade \nE {} que são menores de idade'.format(tot_maior, tot_menor))
