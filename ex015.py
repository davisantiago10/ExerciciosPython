#Aluguel de carros
s = float(input('Quantos km esse carro percorreu?'))
t = int(input('Quantos dias você usou este carro?'))
preço = t * 60 + 0.15 * s
print('O valor a ser pago é de R${}'.format(preço))