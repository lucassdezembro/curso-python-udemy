"""

Introdução ao try/except

try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Insira um número para descobrir seu dobro: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Houve uma falha ao ler o que você digitou.')
