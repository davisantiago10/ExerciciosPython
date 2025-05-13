# numeros = 0
# tot = 0
# soma = 0
tot = soma = 0
numeros = int(input('Digite um número (Digite 999 se quiser parar): '))
while numeros != 999:
    tot += 1
    soma += numeros 
    numeros = int(input('Digite um número (Digite 999 se quiser parar): '))
print('Foram digitados {} números, e a soma entre todos eles é {}'.format(tot, soma))
