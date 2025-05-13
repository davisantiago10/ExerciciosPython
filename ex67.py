while True:
    print('-'*60)
    n = int(input('''Quer ver a tabuada de qual valor? 
(Escreva um número negativo para encerrar):'''))
    print('~~'*60)
    if n < 0:
       break
    for c in range(1,11):
        t = n * c
        print('{} x {} = {}'.format(n, c, t))
print('PROGRAMA ENCERRADO! Obrigado.')
