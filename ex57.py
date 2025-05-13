sexo = str(input('Informe seu sexo [M/F]: ')).strip() .upper() [0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida, digite novamente: ')).strip() .upper() [0]
print('Registrado, fim')
