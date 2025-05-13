import time
idade = int(input('Me diga sua idade, para sabermos em que categoria você ingresserá:'))
print('Tendo uma idade de {} anos...'.format(idade))
time.sleep(2)
if idade < 9:
    print('\033[36m''Sua categoria é a mirim.''\033[m')
elif 10<= idade <= 14:
    print('\033[36m''Sua categoria é a infantil.''\033[m')
elif 15<= idade <= 19:
    print('\033[36m''Sua categoria é a júnior.''\033[m')
elif idade == 20:
    print('\033[36m''Sua categoria é a sênior.''\033[m')
elif idade > 20:
    print('\033[33m''Sua categoria é a MASTER.')
    