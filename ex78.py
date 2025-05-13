lista = []
PosicaoMaior = []
PosicaoMenor = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

for posicao, valores in enumerate(lista):
    if valores == max(lista):
        PosicaoMaior.append(posicao)
    if valores == min(lista):
        PosicaoMenor.append(posicao)

print('=-'*35)
print(lista)
print(f'O maior valor foi o {max(lista)} nas posições {PosicaoMaior}')

print(f'Enquanto o menor valor foi o {min(lista)} nas posições {PosicaoMenor}')



