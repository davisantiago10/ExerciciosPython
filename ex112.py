def LerDinheiro(p=0.0):
    while True:
        p = str(input('Digite o preço: R$')).strip()
        try:
            return float(p.replace(",", "."))
        except ValueError:
            print((('\033[31mNão é um valor float, tente de novo: \033[m')))

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def aumentar(preco=0, taxaa=0, sit=False):
    '''
    --> Calcula o aumento de um determinado preço,
    retorando o resultado com ou sem formatação.
    :param preco: preço que se quer reajustar
    :param taxaa: a porcentagem do aumento
    :param sit: quer a saída formatada ou não?
    :return: o valor reajustado com ou sem formato
    '''

    res = preco + (preco * taxaa/100)
    if sit == True:
        res = moeda(res)
    return res


def diminuir(preco=0, taxad=0, sit=False):
    res = preco - (preco * taxad/100)
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


def resumo(preco=0, taxaa=0, taxad=0, sit=True):
    print('-='* 14)
    texto = 'RESUMO DO VALOR'
    print(f"{texto:>20}")
    print('-='* 14)

    print(f"Preço analisado:    {moeda(preco)}")
    print(f'Dobro do preço:     {dobro(preco, sit=True)}')
    print(f'Metade do preço:    {metade(preco, sit=True)}')
    print(f'{taxaa}% de aumento:     {aumentar(preco, taxaa, sit=True)}')
    print(f'{taxad}% de redução:     {diminuir(preco, taxad, sit=True)}')
    print('-='*14)

p = LerDinheiro()
resumo(p, 35, 22)
