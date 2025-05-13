from datetime import datetime
def voto(ano):
    idade = datetime.now().year - nasc
    if idade >= 18:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO'

    if 16 <= idade <= 17 or idade >= 65:
        return f'Com {idade}, seu voto é opcional'

    if idade < 16:
        return f'Com {idade}, seu voto é PROIBIDO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))