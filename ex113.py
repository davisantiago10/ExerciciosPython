def leiaInt(n = ''):
    while True:
        try:
            n = input('Digite um número inteiro: ')
            int(n)
            break
        except (ValueError, TypeError):
            print(f'\033[31m{n} não é um número inteiro válido\033[m')
        except (KeyboardInterrupt):
            print(None)
            return 0
    return n

def leiafloat(f= ''): 
    while True:
        try:
            f = input('Digite um número real: ')
            float(f)
            break 
        except (ValueError, TypeError):
            print(f'\033[31mEsse não é um número real.\033[m')
        except (KeyboardInterrupt):
            print(None)
            return 0
    return f




n = leiaInt()
f = leiafloat()
print(f'Número inteiro: {n} || Número real: {f}')
  