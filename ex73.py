#Times do Brasileirão em ordem
times = ('Athlético-PR', 'Bahia', 'Flamengo','Botafogo', 'São Paulo','Cruzeiro', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio','Vasco', 'Criciúma', 'Juventude', 'Corinthians','Fluminense', 'Vitória','Atlético-GO', 'Cuiabá')
print('='*30)
#Os 5 primeiros
print('Os 5 primeiros colocados são: {}'.format(times[:5]))
print('='*30)
#Os 4 últimos 
print('Os quatro últimos são: {}'.format(times[16:]))
print('='*30)
#Lista alfabética
print('Em ordem alfabética: {}'.format(sorted(times)))
print('='*30)
#Em que posição está o MENGÃO MALVADÃO
print(times.index('Flamengo'))
posFla = times.index('Flamengo') + 1
print(posFla)
print('O mengão está em {}º lugar'.format(posFla))  