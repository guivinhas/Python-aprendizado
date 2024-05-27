num = input('Digite um número inteiro: ')

try:
    intnum = int(num)
    if intnum % 2 == 0:
        print(f'O {intnum} é um número PAR!')
    else:
        print(f'O {intnum} é um número ÍMPAR!')
except:
    print('Você não digitou um número inteiro!')