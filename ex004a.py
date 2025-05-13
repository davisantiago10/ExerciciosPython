#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele
algo = input('Digite algo: ')
print('O tipo primitivo dela é:{}'.format(type(algo)))
print('É número?')
print(algo.isnumeric())
print('É uma palavra?')
print(algo.isalpha())
print('É algum número decimal?')
print(algo.isdecimal())
print('É algum número algébrico?')
print(algo.isalnum())