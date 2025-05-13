num = int(input('\033[36m' 'Digite um número inteiro:''\033[m'))
num2 = int(input('\033[36m''Digite outro número inteiro''\033[m'))

if num > num2:
    print('O número {} é maior que o {}'.format(num, num2))
elif num2 > num:
    print(' O número {} é maior que o {}'.format(num2, num))
elif num == num2:
    print('Não há número maior, eles são iguais.')
