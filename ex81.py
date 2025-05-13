n = []
while True:
    n.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {len(n)} números')
n.sort(reverse=True)
print(f'Em ordem decrescente: {n}')
if 5 in n:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
    
    