"""

Formatação básica de strings

s - string
d - int
f- float
.<número de dígitos>f]x ou X - Hexadecimal

(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro

Sinal: - ou +
Ex.: 0>-100,.f
Conversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #contando com a variavel
print(f'{variavel: <10}.') #contando com a variavel
print(f'{variavel:$<10}.') #contando com a variavel

print(f'{21321312.1232132132132132:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')

print(f'{variavel!r}')