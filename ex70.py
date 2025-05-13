barato = ''
total_compra = tot1000 = cont = menor = 0
while True:
    print('SALDÃO DA INFORMÁTICA')
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total_compra += preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço >= 1000:
        tot1000 += 1
    
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip() .upper() [0]
    
    if opção == 'N':
        break
print('---- FIM DO PROGRAMA ----')
print('O total de sua compra é de R${}'.format(total_compra))
print('Temos {} produtos que custam mais de R$1000'.format(tot1000))
print('O produto mais barato é {} e custou R${}'.format(barato, menor))

