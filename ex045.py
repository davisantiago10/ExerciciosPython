import random
print("\033[35m" '-='*5, 'PEDRA, PAPEL E TESOURA', '=-'*5 ,'\033[m')
meu = str(input('\033[36m''Minha escolha:')).capitalize()
print('\033[35m''''JO
KEN
PÔ''')
jogadas = [ 'Pedra', 'Papel', 'Tesoura']
pc = random.choice(jogadas).capitalize()

print('\033[36m' 'O computador jogou {}'.format(pc))

if 'Pedra' in meu and 'Pedra' in pc or 'Papel' in meu and 'Papel' in pc or 'Tesoura' in meu and 'Tesoura' in pc:
    print('\033[33m''EMPATE''\033[m')

elif 'Pedra' in meu and 'Papel' in pc:
    print('\033[31m''DERROTA''\033[m')

elif 'Pedra' in meu and 'Tesoura' in pc:
    print('\033[32m''VITÓRIA''\033[m')

elif 'Pedra' in pc and 'Papel' in meu:
    print('\033[32m''VITÓRIA''\033[m')

elif 'Pedra' in pc and 'Tesoura' in meu:
    print('\033[31m''DERROTA''\033[m')

elif 'Papel' in meu and 'Tesoura' in pc:
    print('\033[31m''DERROTA''\033[m')
