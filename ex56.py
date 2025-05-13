somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
idadebaixamulher = 0

for p in range(1,5):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip() .upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomehomemvelho = nome
    elif sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome 
    if sexo in 'F' and idade < 20:
        idadebaixamulher += 1

    mediaidade = somaidade / 4
print('A média de idade é {} anos '.format(mediaidade))
print('O homem mais velho tem {} anos, e se chama {}'.format(maioridadehomem, nomehomemvelho))
print('Existem {} mulheres com menos de 20 anos'.format(idadebaixamulher))


