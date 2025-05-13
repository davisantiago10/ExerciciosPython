nome = input('Digite o seu nome:').strip()
nome1 = nome.upper()
print('\033[34m É verdade que seu nome tem Silva?')
print(bool(nome1.count('SILVA')))
