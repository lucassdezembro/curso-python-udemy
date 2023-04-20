# Operadores in e not in
# Strings são iteráveis -> item por item (looping)

#  0   1   2   3   4
#  L   U   C   A   S
# -5  -4  -3  -2  -1

nome = input('Nome: ')

print(f'A última letra do nome {nome} é {nome[-1]}')

caracteres = input('Busque por uma caracteres: ')

if caracteres in nome:
    print(f'O nome {nome} contem {caracteres}')
else:
    print(f'O {nome} não contem {caracteres}')