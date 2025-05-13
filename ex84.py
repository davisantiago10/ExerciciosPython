dados = []
galera = []
op = ''
cont = 0
pesoma = pesome = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso:')))
    if cont == 0:
        pesoma = dados[1]
        pesome = dados[1]

    if dados[1] > pesoma:
        pesoma = dados[1]

    if dados[1] < pesome:
        pesome = dados[1]

    galera.append(dados[:])
    dados.clear()
    cont += 1
    op = str(input('Quer continuar? '))
    if 'Nn'in op:
        break
print('-='*30)
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso é {pesoma} e pertence a ', end='')
for p in galera:
    if p[1] == pesoma:
        print(f'[{p[0]}]')
print(f'E o menor peso é {pesome} e pertence a', end='')
for p in galera:
    if p[1] == pesome:
        print(f'[{p[0]}]')


