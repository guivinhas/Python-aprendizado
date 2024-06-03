#Gerenciador de lista de compras
import os
lista = []

while True:
    entrada = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar: ')

    if entrada == 'i' or entrada == 'I':
        os.system('cls')
        mercadoria = input('Digite o produto que você quer inserir na lista: ')
        lista.append(mercadoria)
        print('')
        print(f'O item "{mercadoria}" foi inserido com sucesso!')
        print('')
        print('Sua lista está assim!')
        for indice, nome in enumerate(lista):
            print (indice, nome)

    if entrada == 'A' or entrada == 'a':
        for indice, nome in enumerate(lista):
            print (indice, nome)
        try:
            produto_apagar = input('Digite o número do produto que você quer apagar: ')
            i = int(produto_apagar)
            print('')
            print(f'Produto "{lista[i]}" foi apagado com sucesso!')
            lista.pop(i)
        except:
            print('O número que você inseriu está incorreto!')
            continue

    if entrada == 'l' or entrada == 'L':
        print('Sua lista está assim:')
        for indice, nome in enumerate(lista):
            print(indice, nome)

    if entrada not in 'ialIAL':
        print('Digite uma opção válida!')