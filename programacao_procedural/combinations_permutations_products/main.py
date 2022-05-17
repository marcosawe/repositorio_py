"""
Combination, Permutations e Products - Intertools
Combinação - A ordem não importa
Permutação - A Ordem importa
Ambos não repetem valores únicos
Produto - A ordem importa e os valores podem se repetir
"""
from itertools import combinations, permutations,product

pessoa = ['Luiz', 'Gustavo', 'Augusto', 'César', 'Felipe'];

for grupo in combinations(pessoa,2): # Dentro das combinações você seta a variável e o número de combiinações que os elementos podem fazer.
    print(grupo); 

print(["#"*95]);

for grupo in permutations(pessoa,2):
    print(grupo);

print(["#"*95]);

for grupo in product(pessoa,repeat=2): # Setamos o número de repetições que podem ser efetuadas, através do método repeat= (valor)
    print(grupo);