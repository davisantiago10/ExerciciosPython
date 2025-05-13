num1 = int(input('Digite um numero inteiro:'))
num2 = int(input('Digite outro:'))
num3 = int(input('Digite mais um:'))
#num1 for maior e num3 for menor:
if num1 > num2 > num3:
    print('\033[36m O maior número entre esses três é: {}'.format(num1))
    print('\033[34m Enquanto o menor é : {}'.format(num3))
#Para num1 for maior e num2 for menor:
if num1 > num3 > num2:
    print('\033[36m O maior número é : {}'.format(num1))
    print('\033[34m Enquanto o menor é: {}'.format(num2))
#Para num2 for maior e num1 menor:
if num2 > num3 > num1:
    print('\033[36m O maior número é: {}'.format(num2))
    print('\033[34m Enquanto o menor é: {}'.format(num1))
#e
if num2 > num1 > num3:
    print('\033[36m O maior é: {}'.format(num2))
    print('\033[34m Enquanto o menor é: {}'.format(num3))
# num3 maior:
if num3 > num2 > num1:
    print('\033[36m O maior entre eles é: {}'.format(num3))
    print('\033[34m Enquanto o menor é: {}'.format(num1))
if num3 > num1 > num2:
    print('\033[36m O maior entre eles é: {}'.format(num3))
    print('\033[36m Enquanto o menor é: {}'.format(num1))
