def ficha(nome = '', gols = 0):
    nome = input('Nome: ')
    gols = input('Gols: ')
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s).')

ficha()