# Serve para filtrar informações requeridas, sua funcionalidade é parecida com a função map, porém retorna um booleano sobre a expressão afirmada.

from dados import lista,pessoas,produtos

# Filtra os valores maiores que 5
nova_lista = filter(lambda f:f > 5,lista);
print(list(nova_lista));

# Filtrando dicionários
nova_lista2 = filter(lambda f:f['Preco'] > 10, produtos)

for valor_produtos in nova_lista2:
    print(valor_produtos)