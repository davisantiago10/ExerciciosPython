lista = []
for p in range(1,6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    lista += [peso]

print('O maior peso foi {} Kg'.format(max(lista)))
print('E o menor foi {} Kg'.format(min(lista)))
