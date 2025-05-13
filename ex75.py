numeros = int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o último: '))
cont9 = 0
for c in numeros:
    if c == 9:
        cont9 += 1

print('Os valores digitados foram {}'.format(numeros))
print(f'O número 9 apareceu {cont9} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3)+1}')
else: 
    print('Não há valor 3')
print('Os valores pares são ', end='')
for c in numeros:
    if numeros % 2 == 0:
        print(numeros, end=' ')

