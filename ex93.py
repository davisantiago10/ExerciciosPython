dados = {}
partidas = []
dados['nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas ele jogou? '))
for c in range( 0, total):
    partidas.append(int(input(f'Quantos gols fez na partida {c + 1}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)

print(f'O jogador {dados["nome"]} jogou {len(partidas)} partidas. ')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i} fez {v} gols.')
print(f'Totalizando {dados["total"]} gols')
