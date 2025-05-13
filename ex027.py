#Nome completo, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo:')).strip()
nome1 = nome.split()
print('\033[34m Muito prazer em te conhecer')
print('\033[35m Primeiro nome: {}'.format(nome1[0]))
print('Último nome: {}'.format(nome1[-1]))
