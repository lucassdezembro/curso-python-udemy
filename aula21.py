# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados false (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

opcao_entrada = input('[E]ntrar [S]air: ')

senha_digitada = input('Senha: ')

senha_permitida = '1234'

if opcao_entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print('')

print('-*-' * 20)

print('')

# Avaliação de curto circuito
print(True and False and True)
print(True and bool(0) and True)
print(True and bool('') and True)