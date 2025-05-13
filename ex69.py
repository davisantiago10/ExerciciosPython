homens = mulheres20 = tot18 = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo dessa pessoa (m/f): '))
    opção = ' '
    while opção not in 'sn':
        opção = str(input('Quer continuar? (s/n): '))
    if 'm' in sexo:
        homens += 1
    if idade >= 18:
        tot18 += 1
    if 'f' in sexo and idade < 20:
        mulheres20 += 1
    if 'n' in opção:
        break
print('===== fim do programa ====')
print('Total de pessoas com mais de 18 anos: {}'.format(tot18))
print('Ao todo, temos {} homens cadastrados'.format(homens))
print('E temos {} mulheres com menos de 20 anos'.format(mulheres20))

    