# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição veradeira define toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão interia será avaliada naquele valor.
# São considerados falsy 0, 0.0, '', False
# Também existe o tipo None, que é usado para representa um não valor

opcao_entrada = input('[E]ntrar [S]air: ')

senha_digitada = input('Senha: ')

senha_permitida = '1234'

if (opcao_entrada == 'E' or opcao_entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print('')

print('-*-' * 20)

print('')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)