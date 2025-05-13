def CalculaArea(largura, comprimento):
    area = l * c
    print(f'A área do terreno é de {area}m²')

def texto(t):
    print('-='*30)
    print(t)
    print('-='*30)

texto('     CALCULADOR DE ÁREA')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

CalculaArea(l, c)
