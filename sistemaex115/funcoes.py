def Cadastra():
    """Função para cadastrar nome e idade"""
    nome = input('Nome: ').strip()
    while True:
        try:
            idade = int(input('Idade: '))
            return nome, idade  # Retorna os valores para serem salvos
        except ValueError:
            print('\033[31mErro! Digite uma idade válida (número inteiro).\033[m')
        except KeyboardInterrupt:
            print("\n\033[31mO campo 'idade' é obrigatório!\033[m")


def ExibeDados():
    try:
        with open('cadastro.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhum cadastro encontrado.')
            print('-='*15)
            print('     Lista de Cadastros:')
            print('-='*15)
            for linha in linhas:
                nome, idade = linha.strip().split(',')
                print(f'Nome: {nome}, Idade: {idade}')
    except FileNotFoundError:
        print('Arquivo de cadastro não encontrado!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


def Menu():
    while True:
        try:
            op = int(input('\033[35mSua opção: \033[m'))
            if op == 1:
                ExibeDados()
            elif op == 2:
                nome, idade = Cadastra()
                salva(nome, idade)
            elif op == 3:
                print('Encerrando...')
                break
            else:
                print('Valor digitado errado, tente novamente')
        except (ValueError, TypeError):
            print(f'\033[31mNão é uma opção válida\033[m')




# método de armazenar os dados em outro arquivo
def salva(nome, idade):
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}\n')
    print(f'Dados de {nome} salvos com sucesso!')


def titulo():
    print('-='*16)
    print('        Menu Principal')
    print('-='*16)
    print("""\033[36m
1 - Ver pessoas cadastradas
2 - Cadastrar uma nova pessoa
3 - Encerrar\033[m
""")
    print('-='*20)

titulo()
Menu()
