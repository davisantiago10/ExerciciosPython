import random
aluno1 = input('Escreva o primeiro dos quatro alunos que serão sorteados:')
aluno2 = input('Escreva o segundo:')
aluno3 = input('Escreva o terceiro:')
aluno4 = input('Escreva o quarto:')
#Também é necessário fazer a lista
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
