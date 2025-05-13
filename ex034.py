salario = float(input('Qual o seu salário?'))
salario2 = salario + (salario * 15 / 100)
salarionovo = salario + (salario * 10 / 100)
if salario <= 1250.00:
    print('\033[36;40m O seu novo salário é de R${:.2f} \033[m'.format(salario2))
else:
    print('\033[36m O seu novo salário é de R${:.2f}'.format(salarionovo))
