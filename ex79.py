lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print('O Valor já foi digitado, não irei armazenar.')
    
    opcao = input("Quer continuar? [S/N]: ").upper()
    if 'N' in opcao:
        break

print("Sua lista, em ordem crescente, ficou assim:")
print(sorted(lista))
