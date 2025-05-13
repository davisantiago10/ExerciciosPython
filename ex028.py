from random import randint
num = int(input('Escolha um número inteiro entre 0 e 5:'))
num2 = randint(0,5)
if num == num2:
    print('\033[36m Parabéns, o número que você escolheu, foi o mesmo que o computador escolheu.')
else:
    print('\033[32m Você errou! kkkkk')
print('O número sorteado foi {}'.format(num2))
