nota = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota + nota2) / 2
print('Sua média final é de {:.1f}'.format(media))
if media > 7 or media == 7:
    print('\033[36m''Parabéns, você está aprovado!''\033[m')
elif media > 5 and media < 7:
    print('\033[33m''Você ter que fazer a recuperação!''\033[m')
elif media < 5:
    print('\033[31m''Poxa, infelizmente você reprovou este ano.''\033[m')
          