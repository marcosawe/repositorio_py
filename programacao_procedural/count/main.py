"""
Count (Contador) - Itertools
"""
# Diferentemente do módulo Range o Count é um módulo iterável, sendo Range um iterador.
# Para trazer a função count importamos a mesma do Módulo Itertools
from itertools import count

contador = count(start=-10,step=0.01) # Para definir parâmetros dentro urilizamos start = (valor), step = (valor multiplo processado)

for valor in contador:
    print(round(valor,2)) # O método round arredonda o valor dentro dele 
    if valor >= 11:
        break
