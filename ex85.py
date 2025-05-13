numeros = [[], []]

for v in range(0,7):
    valor = int(input(f'Digite o {v + 1} valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else: 
        numeros[1].append(valor)

print(f'Os números pares em ordem crescente são: {sorted(numeros[0])}')
print(f'Os números ímpares em ordem crescente são {sorted(numeros[1])}')

