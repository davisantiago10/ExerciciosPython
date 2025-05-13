import math
an = float(input('Digite o ângulo:'))

#É necessário passar o número para radiando.

seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O valor do seno, do cosseno e da tangente desse ângulo é: \n {:.2f}, \n {:.2f}, \n {:.2f}'.format(seno, cos, tan))
