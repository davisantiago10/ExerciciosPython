data = int(input('Diga o ano de seu nascimento:'))
idade = 2024 - data
print('Você tem aproximadamente {} anos'.format(idade))

if idade > 18:
    sobra = idade - 18
    print('Você já deveria ter se apresentado ao exército há {} anos!'.format(sobra))
elif idade == 18:
    print('Este ano você já deve se apresentar ao exército.')
elif idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} anos para você ter que se apresentar ao exército.'.format(falta))
    