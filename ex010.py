#iteração de Strings

nome = input('Digite seu nome: ')
novonome = ''
tamanho_nome = len(nome)
contador = 0

while contador < tamanho_nome:
    print(novonome)
    novonome += (nome[contador]+'*')
    contador += 1

print(novonome)