med1 = float(input('Digite a primeira medida:'))
med2 = float(input('Digite a segunda:'))
med3 = float(input('Digite a terceira:'))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('\033[4;35;40m -='*5, '\033[1;36m Esses segmentos são capazes de montar um triângulo! \033[35m', '-='*5 )
else:
    print('Essas medidas \033[1;31m não \033[m podem formar um triângulo!')
