alunos = []
# alunos[0] é o nome, alunos[1] é nota 1, e alunos[2] é nota 2
cont = 0

while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    alunos.append([aluno, nota1, nota2])
    op = str(input('Quer continuar? [s/n] '))
    if op in 'Nn':
        break

print('-='*5, 'BOLETIM', '=-'*5)

for aluno in alunos:
    print(f'Nome do aluno {cont}: {aluno[0]}')
    media = (aluno[1] + aluno[2]) / 2
    print(f'Média: {media}')
    cont += 1
    print('='*10)

while True:
    interface = int(input('Quer mostrar a nota de algum aluno? \n(Digite o número do aluno escolhido ou 999 para interromper) '))
    if interface != 999:
        print(f'Notas do(a) {alunos[interface][0]}:')
        print(f'Primeira nota: {alunos[interface][1]}')
        print(f'Segunda nota: {alunos[interface][2]}')
        print('-='*20)
    else:
        break

print('Fim')