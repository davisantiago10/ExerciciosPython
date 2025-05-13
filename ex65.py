opção = 'S'
soma = tot = 0
while 'N' not in opção:
    numeros = int(input('Digite um número inteiro: '))
    tot += 1
    soma += numeros
    if tot == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros
    opção = str(input('Quer continuar? [S/N] ')).upper() .strip()
media = soma / tot

print('Você digitou {} números e a média entre eles foi {:.1f}'.format(tot, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
