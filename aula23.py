# Operador lógico "not"
# Usado para inverter expressçoes
# not True = False
# not False = True

senha = input('Senha:' )

if not senha == '123456':
    print('Senha inválida')

print(not True) # False
print(not False) # True