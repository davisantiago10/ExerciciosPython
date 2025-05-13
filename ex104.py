def leiaInt(n = ''):
    n = input(n)
    while n.isnumeric() == False:
        print('\033[31mIsso não é um número inteiro \033[m')
        n = input('Tente novamente: ')
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')   