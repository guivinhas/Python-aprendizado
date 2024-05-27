#Condicionais

firstvalue = input('Digite um valor: ')
secondvalue = input('Digite outro valor: ')

if firstvalue > secondvalue:
    print('O Primeiro valor =', firstvalue, 'é maior que o segundo valor =', secondvalue)
elif secondvalue > firstvalue:
    print('O Segundo valor =', secondvalue, 'é maior que o primeiro valor =', firstvalue)
else:
    print('Os dois valores são iguais!')