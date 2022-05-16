# São utilizadas para a optimização de performace e escrever menos linhas de código.

l1 = [1,2,3,4,5,6,7,8,9];
ex1 = [variavel for variavel in l1]; # Iteração comum da l1
print(ex1);

ex2 = [v * 2 for v in l1]; # Mutiplica o valor de uma lista por cada elemento presente nela.
print(ex2);

ex3 = [(v,v2) for v in l1 for v2 in range(3)];# Iteração de um conjunto de modelos cordenadas, por iteração entre tuplas.
print(ex3);

l2 = ['Luiza','Mauro','Camilo']

ex4 = [v.replace("a","u") for v in l2] # Iteração sobre o conjunto de palavras dentro de uma lista.
print(ex4)

tupla = (
    ('chave','Valor'),
    ('chave','Valor'),
    ('chave','Valor'),
    ('chave','Valor'),
);

ex5 = [(y,x) for x,y in tupla] # Iteração de trocas de valores dentro de tuplas.
print(ex5); 

l3 = list(range(0,200)) # Faz uma iteração com relação aos valores divisíveis por um determinado número.
ex5 = [v for v in l3 if v %2 == 0 if v %9 == 0]
print(ex5)

ex6 = [v if v %3 == 0 else '0' for v in l3]
print(ex6)

