print('-'*30)
print('Sequência de Fibonaci')
print('-'*30)
quant = int(input('Diga quantos termos você quer: '))
print('~'*30)
t1 = 0
t2 = 1
print('{} --> {}'.format(t1, t2), end='')
cont = 3
while cont <= quant:
    t3 = t1 + t2
    print('--> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('--> Fim')
