n = int(input('Digite um número inteiro para que eu possa montar sua tabuada:'))
print('\033[35m' '  TABUADA DO {}:   ''\033[m'.format(n))
for c in range(1, 11):
    t = n * c
    print('{} x {} = {}'.format(n, c, t))
    