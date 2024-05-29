#Exercício com condição, fatiamento, formatação de f strings.

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
qtdletras = len(nome)-(' ' in nome)

if nome !='' and idade !='':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Sua idade é {idade}')
    print(f'seu nome tem {qtdletras} letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A ultima letra do seu nome é "{nome[-1]}"')
    if ' ' in nome:
        print(f'Seu nome tem espaços')
    elif ' ' not in nome:
        print(f'Seu nome não tem espaços')
else:
    print('você deixou os campos vazios')