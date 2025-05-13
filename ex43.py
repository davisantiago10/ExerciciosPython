import time
print('\033[35m', '-='*5, '\033[36m''VAMOS CALCULAR SEU IMC','\033[35m''=-'*5, '\033[m')

altura = float(input('Digite sua altura: (m)'))
peso = float(input('Digite seu peso: (Kg)'))

imc = peso / altura**2
print('Seu IMC está em: {:.1f}, isso significa que...'.format(imc))
time.sleep(2)

if imc < 18.5:
    print('\033[31m''Você está abaixo do peso ideal!')
elif 18.5 < imc < 25:
    print('\033[32m''Você está no seu peso ideal!')
elif 25 < imc < 30:
    print('\033[33m''Você está com sobrepeso')
elif 40 < imc:
    print('\033[31m''Você está com obesidade mórbida')
