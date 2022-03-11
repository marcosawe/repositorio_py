"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

###################### Primeiro Programa ##########################
numero_inteiro = input('Determine algum número inteiro ');

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
            print(f'{numero_inteiro} é par');
        
    else:
            print(f'{numero_inteiro} é impar');
else:
    print('Isso não é um número inteiro');

##################### Segundo Programa ##########################

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Determine um horário entre (0-23): ')
if horario.isdigit():
    horario = int(horario);
    
    if horario <0 or horario >23:
        print('O horário deve estar entre 0-23.');
    else:
        if horario <=11:
            print('Bom dia !!!');
        elif horario >=12 and horario<=18:
            print('Boa Tarde !!!');
        else:
            print('Boa Noite !!!');
else:
    print("Por favor, digite um horário entre 0-23.");
##################### Terceiro Programa ##########################

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ');
tamanho = len(nome);

if tamanho <=4:
    print('Seu nome é curto');
elif tamanho >=5 and tamanho <=6:
    print('Seu nome é normal');
else:
    print('Seu nome é muito grande');