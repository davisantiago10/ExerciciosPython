#colocar 5 números em uma tupla
from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), 
            randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO maior valor foi : {max(numeros)}')
print(f'E o menor foi: {min(numeros)}')
