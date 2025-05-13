from random import randint
from time import sleep
numeros = []
listapar = []
somap = 0
def sorteia():
    print("SORTEANDO...")
    for c in range(0,5):
        n = randint(0,10)
        numeros.append(n)
        print(f'{n} ', end= '', flush= True)
        sleep(0.3)
    print()
    print(f'Números sorteados: {numeros}')
    print('-='*20)

def somaPar():
    sleep(0.5)
    for v in numeros:
        if v % 2 == 0:
            listapar.append(v)
    print(f'Pares: {listapar}')
    print(f'Soma dos pares: {sum(listapar)}')
    print('-='*30)
    
sorteia()

somaPar()
