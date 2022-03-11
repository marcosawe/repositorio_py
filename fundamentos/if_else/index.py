from operator import truediv

#Somente uma cadeia de códigos é aceita
if  False:
    print('Verdadeiro'); #O prólogo do código deve estar entre as cadeias de caracter do if, elif, else
elif False: 
    print('Não é verdadeiro');
elif True:
    print('mamaco')
###################################################################
"""
Operadores relacionais
== -Igual
>= -Maior ou igual
<= -Menor ou igual
> -Maior
< -Menor
"""
nome = input('Qual o seu nome? ');
idade = input('Qual o sua idade? ');
muito_jovem = 21;
muito_velho = 45;
idade = int(idade);
if idade >= muito_jovem and idade <= muito_velho:
    print(f'É permitido que {nome} pegar bebida alcoolica');
else:
    print(f'{nome} não pode pegar bebida alcoolica');
