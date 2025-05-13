def notas(*n, sit=False):
    s = cont =  0
    lista = []
    for c in n:
        s += c
        cont += 1
        lista.append(c)
    maior = max(lista)
    menor = min(lista)

    media = s / cont
    
    if media > 7:
        situa = 'Boa'
    if 5 <= media <= 7:
        situa = 'Ruim'
    if media < 5:
        situa = 'Terrível'

    dados = {'Total': cont, 'maior': maior , 'menor': menor, 'média': media}
    if sit:
        dados['Situação'] = situa
    return dados 

#Programa principal
resp = notas(5.5, 0.5, 10, 0.5, sit=True)
print(resp)