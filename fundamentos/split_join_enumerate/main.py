"""
Split Join e Enumerate em Phyton
* Split - Dividir uma string #str
* Join - Juntar uam string #str
* Enumerate - Enumerar elementos de uma lista #list / iteráveis 
"""
strings = 'O Brasil é o pais do Futebol, o Brasil tem Penta.';
lista_1 = strings.split(' ');
lista_2 = strings.split(',')
print(lista_1);
print()
print(lista_2);
print()

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.');