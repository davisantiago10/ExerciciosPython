matriz = [[0,0,0], [0,0,0], [0,0,0]]
dados = []
pares = []
c3 = []
l2 = []
pesoma = 0
print('-='*5, 'MATRIZ 3x3', '=-'*5)

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])

        if c == 2:
            c3.append(matriz[l][c])

        if l == 1:
            l2.append(matriz[l][c])
            if l2[-1] > pesoma:
                pesoma = l2[-1]

print('-='*20)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos pares é: {sum(pares)}')
print(f'A soma dos valores da terceira coluna é: {sum(c3)}')
print(f'O maior valor da segunda linha é: {pesoma}')
