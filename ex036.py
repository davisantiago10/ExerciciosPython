#valor da casa, salario e anos
#Calcule o valor mensal, sabendo que ela não pode exceder 30% do salário ou entoao o emprestimo sera negado
print('\033[36m' '=-'*5, "Bom dia", '=-'*5, '\033[m')  
print("Digite abaixo o valor da casa, seu salário e em quantos anos você deseja pagar:")
casa = float(input("Valor da casa:"))
salario = float(input("Seu salário: R$"))
anos = int(input('Quantos anos:'))

prestacao = casa / (anos*12)

limite = 30/100 * salario 
if prestacao < limite:
    print('\033[32m''Seu empréstimo pode ser feito!')
elif prestacao == limite:
    print('Esse empréstimo pode ser feito!')
else:
    print('\033[31m''Seu empréstimo não poderá ser feito!')
