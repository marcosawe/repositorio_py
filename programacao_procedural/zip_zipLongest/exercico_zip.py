"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
"""
# Resposta:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
lista_somaAB = [x+y for x,y in zip(lista_a,lista_b)]
print(lista_somaAB)

# Resposta com zip_longest:
from itertools import zip_longest
lista_somaAB_ziplongest = [x+y for x,y in zip_longest(lista_a,lista_b, fillvalue=0)]
print(lista_somaAB_ziplongest)

# Resposta para qualquer tipo de linguagem de programação.
# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
