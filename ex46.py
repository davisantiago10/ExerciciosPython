import time
print('\033[36m' 'CONTAGEM REGRESSIVA PARA O ANO NOVO!''\033[m')
for c in range(10, -1, -1):
    time.sleep(1)
    print('\033[34m', c)
time.sleep(1)
print('\033[33m''FELIZ ANO NOVO!' '\033[m')
