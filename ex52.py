# Ver se um número é primo
print('=-'*5 ,'ANALISADOR DE NÚMEROS PRIMOS', '-='*5)

numero = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[36m', end=(' '))
        tot += 1
    elif numero % c != 0:
        print('\033[31m', end=(' '))
    print('{}'.format(c), end=(' '))
print('\033[m''\n', 'O número {} foi divisivel {} vezes'.format(numero, tot))

if tot == 2:
    print('O número {} é primo'.format(numero))
else:
    print('Não é primo!')
