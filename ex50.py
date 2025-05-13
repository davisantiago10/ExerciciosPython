soma = 0
for c in range(1,7):
    c = int(input('Digite um número inteiro: '))
    if c % 2 == 0:
        soma = soma + c
print('A soma dos números pares que você digitou é {}'.format(soma))    
