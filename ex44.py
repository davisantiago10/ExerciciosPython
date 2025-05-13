print('=-'*5, 'LOJAS FURTADAS', '-='*5)
preco = float(input('\033[33m''Qual o preço original do produto?''\033[m'))
pagamento = str(input('\033[33m''Qual será a forma de pagamento\n [ 1 ] Dinheiro \n [ 2 ] Cartão à vista \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais \n''\033[m'))


if '1' in pagamento:
    desconto1 = preco - (10 * preco/100)
    print('O produto terá 10% de desconto')
    print('Ficando com o valor de R${:.2f}'.format(desconto1))
elif '2' in pagamento:
    desconto2 = preco - (5 * preco/100)
    print('O produto terá 5% de desconto')
    print('Ficando com o valor de R${:.2f}'.format(desconto2))
elif '3' in pagamento:
    print('O produto não terá desconto caso esse modo de pagamento seja feito.')
elif '4' in pagamento:
    totparc = int(input('Total de parcelas:'))
    juros = preco + (20 * preco/100)
    parcela = juros / totparc
    print('Será acrescentado um juros de 20% do valor do produto.')
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar R{:.2f} no final.'.format(preco,juros))
