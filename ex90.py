nome = str(input('Nome: '))
media = float(input('Média: '))
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado(a)'

dict = {'nome': nome, 'media': media , 'situacao': situacao}
print('=-='*20)

for k, v in dict.items():
    print(f'{k} é igual a {v}')
    


