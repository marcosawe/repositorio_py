'''
Crie uma função que exibe uma saudação com os parâmetros saudação e nome
'''
def saudacoes(saudacao,nome):
    print(saudacao,nome)

saudacoes('Fala','Mamaco!!')

"""
Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""
def soma(valor1,valor2,valor3):
    print(f'O valor da soma de todos os números é {valor1+valor2+valor3}');

soma(3,65,8)

"""
Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex 10%). Retorne o valor do primeiro número somado ao aumento percentual do segundo
"""
def porcentagem(valor1, valor2):
    valor2 = valor1 * valor2/100
    somaValores = valor1+valor2 
    return print(f'Primeiro Valor {valor1}, Porcentagem do Segundo Valor {valor2}, Soma dos Dois Valores {somaValores}')
porcentagem(4,7)
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne Fizz, se o parâmetro da função for divisível por 5 retorne buzz. Se o parâmetro da função for divisível por 3 e por 5, retorne FizzBuzz, caso contrário retone número inválido.   
"""
def fb(fb):
    if fb % 3 and fb % 5 == 0:
        return print(f'FizzBuzz, o Número {fb} é divisível por 5 e por 3')
    if fb % 3 == 0:
        return print(f'Fizz, o Número {fb} é divisível por 3') 
    if fb % 5 == 0:
        return print(f'Buzz, o Número {fb} é divisível por 5') 
    return print(f'{fb}')

fb(15);

# Gerando uma função de numeração

from random import randint

for i in range(0,100):
    aleatorio = randint(0,100)
    print(fb(aleatorio))