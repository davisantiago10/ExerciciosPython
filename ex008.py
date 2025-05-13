#Código que transforma um valor em metros, para centímetros e milímetros
m = int(input('Digite um valor em metro(s) para a conversão poder ser realizada:'))
c = m * 100
mm = m * 1000
print('Convertendo {} metros para centímetros e milímetros, temos, respectivamente:\n {} cm, e \n {} mm'.format(m, c, mm) )
