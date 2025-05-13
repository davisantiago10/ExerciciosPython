dados = {}
vendas = {}
def usuario():
    print('-=' *20)
    print('CADASTRO DE USUÁRIO')
    dados['Nome'] = str(input('Digite o nome do usuário: '))

    dados['Cpf'] = input('Digite o CPF do usuário: ')
    while dados['Cpf'].isnumeric() == False:
        dados['Cpf'] = input('Houve um erro, digite o CPF novamente: ')

    dados['Celular'] = (input('Número de celular: '))
    while dados['Celular'].isnumeric() == False:
        dados['Celular'] = input('Houve um erro, digite o número novamente: ')

    dados['Email'] = str(input('Email: '))

    dados['Data'] = str(input('Data de nascimento: '))

    print(dados)


def venda():
    print('-='*20)
    print('CADASTRO DE PRODUTO')

    vendas['Usuário vendedor'] = str(input('Nome do usuário que está cadastrando o produto: '))
    
    vendas['Produto'] = str(input('Nome do produto: '))
    
    vendas['Preço de compra'] = float(input('Preço de compra do produto: '))
    
    vendas['Preço de venda'] = float(input('Preço de venda: '))

    print(vendas)

def titulo():
    print('\033[36m-='*15)
    print('  CADASTRO DE FUNCIONÁRIO')
    print('-='*15, '\033[m')


def escolha():
    while True:
        op = str(input('Deseja cadastrar um usuário [1], um vendedor [2] ou encerrar o programa [FIM]? ')).upper()
        if op == '1':
            usuario()
        if op == '2':
            venda()
        if op == 'FIM':
            print('Encerrando...')
            break
        else:
            op = input("Opção inválida, digite apenas 1, 2 ou 'FIM': ")


titulo()
escolha()


