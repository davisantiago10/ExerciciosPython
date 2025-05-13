matriz = [[], [], []]
dados = []
print('-='*5, 'MATRIZ 3x3', '=-'*5)
for l1 in range(0,3):
    dados.append(int(input(f'Digite o valor para a posição {l1 / 10 + 1}: ')))
    matriz[0].append(dados[:])
    dados.clear()

for l2 in range(0,3):
    dados.append(int(input(f'Digite o valor para a posição {l2 /10 + 2}: ')))
    matriz[1].append(dados[:])
    dados.clear()

for l3 in range(0,3):
    dados.append(int(input(f'Digite o valor para a posição {l3 / 10 + 3}: ')))
    matriz[2].append(dados[:])
    dados.clear()

print('-='*20)

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end='')
    print()

#print(' ', matriz[0],'\n ',matriz[1],'\n ',matriz[2])

#print(f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}')
#print(f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}')
#print(f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}')