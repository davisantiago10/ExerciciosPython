num1 = int(input('Digite um valor: '))
num2 = int(input('Mais um: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''O que você quer fazer com eles? 
[1] somar
[2] multiplicar
[3] maior 
[4] novos números
[5] sair do programa : '''))
    if escolha == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, soma))

    elif escolha == 2:
        produto = num1 * num2
        print('A multiplicação deles é igual a {}'.format(produto))

    elif escolha == 4:
        print('Digite novamente:')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))

    elif escolha == 3:
        maior = max(num1, num2)
        print('O maior número é o {}'.format(maior))
    elif escolha == 5:
        print('Fim')
    else:
        print('Opção inválida, tente novamente.')


