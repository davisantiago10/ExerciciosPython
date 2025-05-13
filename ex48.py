cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1
        soma = soma + c
print('\033[36m''A soma de todos esses {} números é {}'.format(cont, soma))
