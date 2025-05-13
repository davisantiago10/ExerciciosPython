med1 = float(input('Digite a primeira medida:'))
med2 = float(input('Digite a segunda medida:'))
med3 = float(input('Digite a terceira medida:'))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('\033[35;40m''-='*5, '\033[36m''Esse triângulo pode ser formado.','\033[35;40m''-='*5, '\033[m')
else:
    print('Esse triângulo não pode ser formado')
    exit()
if med1 == med2 and med2 == med3:
    print('O triângulo formado será um triângulo equilátero.')
elif med1 == med2 or med1 == med3 or med2 == med3:
    print('Esse triângulo será isósceles.')
else:
    print('Esse é um triângulo escaleno.')
