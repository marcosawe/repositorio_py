# Uma forma mais fácil de manipular dicionários.
lista = [
    ('chave','valor'),
    ('chave2','valor2'),
    ('chave2','valor2'),
    ('chave2','valor2'),
]

d0 = {x:y for x,y in lista} # Transformando uma lista com conjuntos de tuplas em dicionários

d1 = {x:y for y,x in lista} # Invertendo os valres da chave e do valor.
print(d1)

d2 = {x.upper():y.upper() for y,x in lista} # Invertendo os valres da chave e do valor.
print(d2)

d3= [x for x in range(0,100) if x %3 == 0]
print(d3)

