num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para a conversão
[ 1 ] NÚMERO BINÁRIO
[ 2 ] NÚMERO OCTAL
[ 3 ] NÚMERO HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:] ))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente')
