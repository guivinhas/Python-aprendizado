#Verificador de CPF
import sys

while True:
    verificarcpf = input('Digite o CPF que deseja verificar: ')

    sequencial = verificarcpf == verificarcpf[0] * len(verificarcpf) 

    if sequencial:
        print('Você digitou um número sequencial!')
        sys.exit()
    for i in verificarcpf:
        cpflimpo = verificarcpf.replace('.', '').replace('-','')
    
    multiplicador = 10
    somadetodos = 0
    ultimosdigitos = ''
    resultado = 0

    for indice, digito in enumerate(cpflimpo):
        j = int(digito)
        if indice <= 8:
            somadetodos += (j * multiplicador)
            multiplicador -= 1
        else:
            print('verificando!')
            ultimosdigitos += digito

    resto = (somadetodos * 10) % 11
    
    if resto > 9:
        resultado = 0
    else:
        resultado = resto

    digitoverificado1 = str(resultado)

                ####segundo digito

    multiplicador2 = 11
    somadetodos2 = 0
    for indice, digito in enumerate(cpflimpo):
        k = int(digito)
        if indice <= 9:
            somadetodos2 += (k * multiplicador2)
            multiplicador2 -= 1
        else:
            print('verificando!')
    
    resto2 = (somadetodos2 * 10) % 11
    digitoverificado2 = str(resto2)
    cpfverificado = digitoverificado1 + digitoverificado2


    if cpfverificado == ultimosdigitos:
        print('O CPF digitado é válido!')
    else:
        print(f'Esse CPF que você digitou é inválido! {verificarcpf}')

    