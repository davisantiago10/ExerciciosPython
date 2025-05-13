cidade = input('Digite o nome da cidade:')
cidade1 = cidade.strip()
cidade2 = cidade1.capitalize()
cidade3 = cidade2.split()
cidade4 = cidade3[0]
print('\033[33m {} começa com Santo?'.format(cidade1))
print(bool(cidade4.count('Santo')))
