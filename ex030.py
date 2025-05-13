num = int(input('Digite um número:'))
num1 = num % 2
if num1 == 0:
    print('\033[m O número {} é par!'.format(num))
else:
    print('\033[m O número {} é ímpar!'.format(num))
