frase = str(input('Digite uma frase:')).strip()
frase1 = frase.upper()
R = frase1.count('A')
primeira = frase1.find('A')+1
ultima = frase1.rfind('A')+1

print('\033[35m A letra A aparece {} vezes'.format(R))
print('Ela aparece pela primeira vez na posição: {}'.format(primeira))
print('E aparece pela última vez na posição: {}'.format(ultima))
