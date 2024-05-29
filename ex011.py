#Calculadora analógica

while True:
    operacao = input(' [+] Soma\n [-] Subtração \n [*] Multiplicação\n [/] Divisão\n [**] Potenciação\n \033[91m[s] Sair \033[0m\n Digite a operação que você quer executar: ')
    if operacao == 'S' or operacao == 's':
        break
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
   
    try:
        floatnum1 = float(num1)
        floatonum2 = float(num2)
        if operacao == '+':
            print(floatnum1+floatonum2)
        elif operacao == '-':
            print(floatnum1-floatonum2)
        elif operacao == '*':
            print(floatnum1*floatonum2)
        elif operacao == '/':
            if floatonum2 != 0:
                print(floatnum1/floatonum2)
            else:
                print('ERRO! Divisão por 0!')
                continue
        elif operacao == '**':
            print(floatnum1**floatonum2)
        else:
            print('Você digitou algo de errado!')
            continue
    except:
        print('Você não digitou números válidos!')
        continue
    

    sair = input('Deseja sair? [S]/[N]').lower().startswith('s')
    if sair:
        break
print('\033[91m O programa está sendo finalizado!\033[0m')