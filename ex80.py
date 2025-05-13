lista = []
for c in range(0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]: #lista[-1] pega o último valor
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição: {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitado em ordem foram: {lista} ')


       
