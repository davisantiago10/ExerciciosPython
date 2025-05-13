from time import sleep
def maior(* valores):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for v in valores:
        print(f'{v} ', end='', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(1,8,3,9,2)
maior(9,4,8)
maior()
