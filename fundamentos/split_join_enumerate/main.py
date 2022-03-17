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
#####################################################
palavra = '';
contagem = 0;
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} e repetiu {contagem} vezes');