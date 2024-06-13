#Gerador de CPF válido

import sys
import random

cpflimpo = ''
for i in range(9):
     cpflimpo += str(random.randint(0,9))

 
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
print(resto, resultado, ultimosdigitos,)

                ####segundo digito

multiplicador2 = 11
somadetodos2 = 0
for indice, digito in enumerate(cpflimpo+digitoverificado1):
    k = int(digito)
    if indice <= 9:
        somadetodos2 += (k * multiplicador2)
        multiplicador2 -= 1
    else:
        print('verificando!')
    
resto2 = (somadetodos2 * 10) % 11
digitoverificado2 = str(resto2)
cpfverificado = digitoverificado1 + digitoverificado2

print(f'{cpflimpo}{digitoverificado1}{digitoverificado2}')

    