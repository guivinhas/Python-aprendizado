#introdução ao try e except

num = input('Digite um número para saber o seu dobro: ')


try:
    numfloat = float(num)
    print(f'O dobro de {numfloat:.0f} é {numfloat*2:.0f}')
except:
    print('Você não digitou um número!')