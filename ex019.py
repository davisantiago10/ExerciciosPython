import random
aluno1 = input('Escreva o primeiro dos quatro alunos que serão sorteados:')
aluno2 = input('Escreva o segundo:')
aluno3 = input('Escreva  o terceiro:')
aluno4 = input('Escreva o quarto:')
#Precisa fazer a lista deles
lista = [aluno1, aluno2, aluno4, aluno3]
escolhido = random.choice(lista)


print('O aluno sorteado foi o {}'.format(escolhido))




