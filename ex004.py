#Operadores lógicos

sessao = input('Entrar ou sair: [E]/[S]')
senhadigitada = input ('Senha: ')

senha = '123456'
print(sessao, senhadigitada)

if (sessao == 'E' or sessao == 'e') and (senhadigitada == senha):
    print('Login bem sucedido!')
elif (sessao == 'E' or sessao == 'e') and (senhadigitada != senha):
    print('Senha errada!')
elif sessao == 'S' or sessao == 's':
    print ('Você saiu!')
else:
    print('Você digitou algo errado!')