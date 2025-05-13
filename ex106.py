def ajuda(com):
    print(comando.__doc__)

def titulo(msg, cor):
    tam = len(msg) + 2
    print('~' * tam)
    


comando = ''
while True:
    comando = str(input('Digite o comando ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
