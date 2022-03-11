"""
While é utilizado para realizar ações enquanto uma condição for aceita.

Requisitos: Entender condições e operadores
"""
    #x = 0;
    #while x<10:
        #y=0;
        #while y<5:
            #print(f'({x},{y})');
            #y+=1;
        #x+=1
#print(f'Acabou!!')
#################### Calculadora Básica #########################
while True:
    primeiro_num = input('Digite o Primeiro Número ');
    segundo_num = input('Digite o Segundo Número ');
    operador = input('Digite um operador: ');
    if not primeiro_num.isnumeric or not segundo_num.isnumeric:
        print('Você precisa digitar um número.')
        continue
    primeiro_num = int(primeiro_num);
    segundo_num = int(segundo_num);
    if operador == '+':
        print(primeiro_num + segundo_num);
    elif operador == '-':
        print(primeiro_num - segundo_num);
    elif operador == '*':
        print(primeiro_num * segundo_num);
    elif operador == '/':
        print(primeiro_num / segundo_num);
    else:
        print('Operador Inválido');
    sair = input('Deseja Sair? [s]im [n]ão: ')
    if sair == 's':
        break


