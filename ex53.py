# arara arara
frase = str(input('Digite uma frase: ')).strip() .upper()
palavras = frase.split()
frase_junta = "".join(palavras)
inverso = ''
# Inverso:
for letra in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[letra]

if frase_junta == inverso:
    print('Temos um palíndromo')
else:
    print('Não é palindromo')

