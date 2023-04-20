nome = 'Lucas'
altura = 1.69
peso = 64.7

imc = peso / altura**2

# usando f-strings
linha_1 = f'{nome} tem {altura:.2f}m de altura,'
linha_2  = f'pesa {peso}kg e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)