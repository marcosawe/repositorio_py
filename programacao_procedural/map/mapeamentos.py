# Mapa em Python é uma função que funciona como um iterador para retornar um resultado após aplicar uma função a cada item de um iterável (tupla, listas, etc.). É usado quando você deseja aplicar uma única função de transformação a todos os elementos iteráveis. A função iterável e a função são passadas como argumentos para o mapa em Python.

"""
A sintaxe da função Python map () é:

map (função, iteráveis)

Em a sintaxe acima:

função: É a função de transformação através da qual todos os itens do iterável serão passados. iteráveis: É o iterável (sequência, coleção como lista ou tupla) que você deseja mapear.

"""
from dados import lista

"""TRABALHANDO COM LISTAS"""

# Para fazer um mapeamento por operação utilizamos
nova_lista = map(lambda x: x*2,lista);
print(lista);
print(list(nova_lista)); # A função map não retorna um lista pronta mas sim um iterador que pode sofrer casting.
lista2 = [x * 2 for x in lista ] # Utilizando list comprehension
print(lista2)

# Utilizando funções
def mul (i):
    return i * i

x=map (mul, (3, 5, 7, 11, 13))
print (list (x))