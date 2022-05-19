# Tal como as suas congéneres map() e filter(), a função reduce() é uma built-in function da linguagem Python, que associa uma função e uma lista.

#Relativamente à sintaxe, a reduce() é simples: reduce(função, lista, opcional). O valor opcional é um valor que, caso a lista seja nula, é tido como valor padrão. A função passada recebe dois argumentos: o primeiro, é o argumento actual da lista, enquanto que o segundo é o resultado da última chamada da função (caso exista)

from functools import reduce

lista = [1, 2, -3, 4, 5, -9]
def soma(a, b):
    return a + b
 
print(reduce(soma, lista))

 
# Explicação
# ((((1 + 2) + (-3)) + 4) + 5) + (-9)) = 0

# Dados
listaDados = [
    {'Nome':'Felipe', 'Idade': 18},
    {'Nome':'Camilla', 'Idade': 22},
    {'Nome':'Jorge', 'Idade': 37},
    {'Nome':'André', 'Idade': 15},
]
# Utilizando lambda
somaidades = reduce(lambda acumulador,pessoas: acumulador + pessoas['Idade'], listaDados, 0)
print(somaidades)