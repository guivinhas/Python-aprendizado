inputhoras = input('Digite a hora atual no formato de número inteiro: EX: 12:00 = 12 ')

try: 
    hora = int(inputhoras)
    if hora >= 0 and hora <= 11:
        print('Bom Dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Você não digitou uma hora válida!')
except:
    print('Você não digitou uma hora válida!')