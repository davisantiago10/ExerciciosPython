from random import choice
print('-='*20)
print('     Vamos jogar par ou ímpar!')
print('-='*20)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tot = 0
while True:
    meu = int(input('Diga um valor: '))
    meu2 = str(input('Par ou Ímpar? [P/I] ')).upper()
    computador = choice(numeros)
    soma = meu + computador
    if soma % 2 == 0:
        result = 'par'
    elif soma % 2 != 0:
        result = 'ímpar'
    print('Você jogou {} e o computador jogou {}, total de {} Deu {}'.format(meu, computador, soma, result ))
    print('--'*30)
    if 'P' in meu2 and 'par' in result:
        print('Você ganhou!')
        tot += 1
    elif 'I' in meu2 and 'impar' in result:
        print('Você ganhou!')
        tot += 1
    else:
        break
print('Você perdeu depois de {} jogadas'.format(tot))
