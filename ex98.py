from time import sleep
def Contador(inic, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-='*20)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}: ')

    if inic <= fim:
        cont = inic
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += passo
        print()
    else:
        cont = inic
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont = cont - passo
        print()

Contador(1,10,1)
Contador(10,0,2)

print('-='* 20)

print('Contagem personalizada:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
Contador(ini, fim, passo)