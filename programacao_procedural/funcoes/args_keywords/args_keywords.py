'''
Funções (def) em python - *args  **keywords 
'''
def func(ag1,ag2,ag3= 7, ag4=8): # A partir do momento que é setado um valor padrão ao argumento eu preciso setar aos demais argumentos entegrados. 
    print(ag1,ag2,ag3,ag4);

func(1,2,10)

# Argumentos *args (Utilizado para definir um conjunto de argumentos até então desconhecidos)
def funcao(*args):
    print(*args)

lista = [1,2,3,4,5]
print(*lista, sep="_") #printa os argumentos dentro da lista separando por "_"

# **keyargs Busca argumentos nomeados dentro de uma função. Como se fosse um dicionário

"""def funci(*args,**keyargs):
    print(args);
    print(keyargs["nome"], keyargs["Sobrenome"]);

funci(*lista,nome= "Luiz", Sobrenome="Alberto")""" 

def funci(*args,**keyargs): #forma mais moderna.
    print(args);

    nome = keyargs.get("nome");
    sobrenome = keyargs.get("sobrenome")
    print(nome, sobrenome);

funci(nome="Marcos Eduardo Fernandes",sobrenome="Domingues");