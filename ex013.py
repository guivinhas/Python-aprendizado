#Jogo adivinhação de palavra inserindo letra por letra

tentativas = 0
palavracorreta = 'miguel'
letrasacertadas = ''
while True:

    letra_tentada = input('Digite apenas uma letra para adivinhar a palavra correta: ').lower()
    try:
        if letra_tentada not in 'abcdefghijklmnopqrstuvwxyz':
            print('Você não colocou uma letra válida!')
            continue
        if letra_tentada == '':
            print('Você não colocou uma letra válida!')
        if len(letra_tentada)> 1:
            print('Você digitou mais de uma letra!')
            continue
    except:
        break
    
    if letra_tentada in palavracorreta:
        letrasacertadas += letra_tentada

    palavraformada = ''

    for i in palavracorreta:
        if i in letrasacertadas:
            palavraformada += i 
        else:
            palavraformada += '*'
    print(palavraformada)
    
    if letra_tentada not in palavracorreta:
        print('Você errou a letra!')
    
    if palavraformada == palavracorreta:
        print('Parabéns! VOCÊ ACERTOU!')
    tentativas += 1
    print(f'Tentativas: {tentativas}')
    continue     