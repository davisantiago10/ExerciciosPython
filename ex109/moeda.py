def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def aumentar(preco=0, taxa=0, sit=False):
    res = preco + taxa * 0.1
    if sit == True:
        res = moeda(res)
    return res


def diminuir(preco=0, taxa=0, sit=False):
    res = preco - taxa * 0.1
    if sit == True:
        res = moeda(res)
    return res

def dobro(preco=0, sit=False): 
    res = preco * 2
    if sit == True:
        res = moeda(res)
    return res

def metade(preco=0, sit=False): 
    res = preco / 2
    if sit == True:
        res = moeda(res)
    return res
