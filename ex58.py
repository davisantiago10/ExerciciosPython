from random import randint
cont = 1
print('\033[36m''Jogo da adivinhação 2.0''\033[m')
pessoa = int(input('Escolha um número de 0 a 10: '))
if pessoa > 10:
    print('\033[31m''Opção inválida')
computador = randint(0,10)
while pessoa != computador:
    pessoa = int(input('\033[31m''Errou, tente de novo: '))
    cont += 1
if pessoa == computador:
    print('\033[34m''Você acertou, parabéns!')
    print('Foram necessárias {} tentativas.'.format(cont))
