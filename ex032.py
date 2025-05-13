ano = int(input('Digite um ano qualquer:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[36m Esse ano é bissexto!')
else:
    print('\033[31m Esse ano não é bissexto')
