from dados import lista,produtos,pessoas
"""TRABALHANDO COM LISTAS"""
# Para fazer um mapeamento por operação utilizamos
nova_lista = map(lambda x: x*2,lista);
print(lista);
print(list(nova_lista)); # A função map não retorna um lista pronta mas sim um iterador que pode sofrer casting.
lista2 = [x * 2 for x in lista ] # Utilizando list comprehension
print(lista2)
"""TRABALHANDO COM DICIONÁRIOS"""
precos = map(lambda p: p["Preço"],produtos);

for valor in precos:
    print(valor)