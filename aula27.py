"""

Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str

"""

var = 'Hello world'

print(var[0]) # H
print(var[-11]) # H

# fatiamento
print(var[0:5]) # normalmente o índice final não é incluído, por isso [5] e não [4]
print(var[:5])
print(var[-5:])
print(var[-5:len(var):2]) # do -5 ao final pulando de 2 em 2
print(var[::-1]) # de trás para frente

# len
print(len(var))