# São formas de como unir iteráveis utilizando o python

"""
Zip - Uninido iteráveis
Zip_longest - Itertools 
"""

### Códigos
cidades = ['São paulo', 'Belo Horizonte','Salvador']
### Códigos
estados = ['SP','MG','BA']

# Zip
cidades_estado = zip(estados,cidades)
cidades_estado = dict(cidades_estado)
print(cidades_estado)

# Zip Longest
# Para utilizar o método Zip_Longest, precizamos importar o módulo Itertools.

from itertools import zip_longest , count

### Códigos
cidades = ['São paulo', 'Belo Horizonte','Salvador','Manaus','Palmas']
### Códigos
estados = ['SP','MG','BA']

cidades_estado = zip_longest(estados,cidades, fillvalue= 'Estado') # Para colocar um valor padrão setado, para que a lista não utilize None utilizamos (fillvalue)
cidades_estado = dict(cidades_estado)
print(cidades_estado)

# Iterando com geradores
indice = count()
cidades = ['São paulo', 'Belo Horizonte','Salvador','Manaus','Palmas']
estados = ['SP','MG','BA']
cidades_estado = zip(
    indice,
    estados,
    cidades, 
    )

for indice, estados, cidades in cidades_estado:
    print(indice,estados,cidades);
