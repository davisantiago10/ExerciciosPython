galera = []
pessoa = {}
media = soma = 0


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('Erro, responda apenas S ou N')
    if resp == 'N':
        break


print('-='* 30)
print(f'Foram cadastradas {len(galera)} pessoas')

media = soma / len(galera)
print(f'A média de idade é de {media :.2f} anos')

print('As mulheres cadatradas foram')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')

print('Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ')
print('FIM')







