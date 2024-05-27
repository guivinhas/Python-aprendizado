usuario = input('Digite seu nome de usuario: ')

if len(usuario) < 4:
    print(f'O nome de usuario "{usuario}" é muito pequeno!')
elif len(usuario)<7:
    print(f'O nome de usuario "{usuario}" é normal!')
else:
    print(f'O nome de usuario "{usuario}" é muito grande!')