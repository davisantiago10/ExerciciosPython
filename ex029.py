num = int(input('Em que velocidade o carro estava?'))
multa = (num - 80) * 7
if num > 80:
    print('\033[33m Ops, você vai ser multado')
    print('\033[31mDe acordo com a velocidade... Sua multa será de R$ {:.2f}'.format(multa))
else:
    print('\033[32m Sua velocidade estava normal, tenha um bom dia!')
