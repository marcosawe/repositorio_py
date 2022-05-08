"""
São conhecidas como funções anônimas que retornam uma função por parâmetro para outra função ou método.
"""
lista = [
    ["P0",50],
    ["P1",40],
    ["P2",56],
    ["P3",20],
    ["P4",80],
    ["P5",13.3],
]
# Existem duas formas de ordenar uma lista a primeira delas é com o método .sort()
# O método .sort() altera a lista original
def func(item):
    return item[1]

lista.sort(key=func,reverse=True) # O atributo reverse faz uma reversão sobre determinada função. 
print(lista)

#####################################################

# Utilizando lambda
lista2 = [
    ["P0",50],
    ["P1",40],
    ["P2",56],
    ["P3",20],
    ["P4",80],
    ["P5",13.3],
]
lista2.sort(key=lambda item: item[1])
print(lista2)
######################################################
# Agora com o método .sorted que não altera o valor original da lista
lista3 = [
    ["P5",13.3],
    ["P1",40],
    ["P0",50],
    ["P2",56],
    ["P4",80],
    ["P3",20],
]
print(sorted(lista3, key=lambda item: item[0]))