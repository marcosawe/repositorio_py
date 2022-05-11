
""" 
Atribuições de métodos 
# add(Adiciona),update(atualiza),clear,discart(descarta o indice desejado)
# Union | (une dois conjuntos)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elemnetos que estão)
"""

# Sets ou conjuntos são um modelo de aplicações de listas matemáticas que normalmente são aplicadas da mesma forma que os dicionarios e listas porém sem o conceito de chave valor e não apresentam indice.

# Para criar um conjuto(set) dentro de phyton utilizamos
s1 = {1,2,3,4,5} 
print(s1)
s2 = set()

# Para adicionar valores dentro de um set utilizamos
s2.add(2)
s2.add((1,2,3,4,422,42))
print(s2)

# Para remover valores dentro de um set utilizamos
s2.discard((1,2,3,4,422,42))
print(s2)

# Para adicionar valores que iterem dentro de um set utilizamos
s1.update("Marcão") # A função update não repeita a ordem da string
print(s1)

# Para remover os valores duplicados de uma lista, basta transformar ela em set
lista = [1,2,2,2,3,4,5,6,6,6,7,8,9,0,0]
lista = sorted(set(lista)) # Utilizar a função sorted dentro de um set faz com que o mesmo seja organizado numericamente
lista = list(lista)
print(lista[1:])

# Para fazer a união entre dois sets diferentes utilizamos
s3 = s1 | s2
print(s3)

# Para unir os elementos presentes em dois sets diferentes utilizamos
s4 = {1,2,3,4,5,6,7,5,6,7,9,12} 
s5 = {1,2,3,4,5,6,7,8,9,10} 
s6 = s4 & s5
print(s6)

# Para definir o único elemento do set presente em um dos sets utilizamos
s6 = s5 - s4
print(s6)

# Para deminir os elementos que estão presentes em um dos set mas não em todos utilizamos
s6 = s5 ^ s4
print(s6)