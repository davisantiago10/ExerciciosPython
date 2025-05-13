def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def aumentar(preco=0, taxa=0):
    res = preco + taxa * 0.1
    return res


def diminuir(preco=0, taxa=0):
    res = preco - taxa * 0.1
    return res

def dobro(preco=0): 
    res = preco * 2
    return res

def metade(preco=0): 
    res = preco / 2
    return res


