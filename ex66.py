soma = tot = 0
while True:
    n = int(input('Digite um  valor (999 pra parar): '))
    if n == 999:
        break
    tot += 1
    soma += n
print(f'A soma desses {tot} números é {soma}')
