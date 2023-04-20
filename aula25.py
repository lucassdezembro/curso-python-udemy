"""

Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)

"""

nome = 'Lucas'
preco = 1000.999199912
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)

print(variavel)

print('\n')

print('O hexadecimal de %d é %04x' % (15, 15))