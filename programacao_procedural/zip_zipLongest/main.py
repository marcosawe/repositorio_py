# São formas de como unir iteráveis utilizando o python

"""
Zip - Uninido iteráveis
Zip_longest - Itertools 
"""

### Códigos
cidades = ['São paulo', 'Belo Horizonte','Salvador']
### Códigos
estados = ['SP','MG','BA']

cidades_estado = zip(estados,cidades)
cidades_estado = dict(cidades_estado)
print(cidades_estado)
