numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro','Cinco', 'Seis', 'Sete', 'Oito', 'Nove','Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20: 
    num = int(input('Tente novamente:'))
print('Você digitou o número {}'.format(numeros[num]))
