"""
Se consiste em uma estrutura de dados que suporta chave e valor.
"""
# Para criar e alimentar um dicionario utilizamos:

# Modo menos usual
d0=dict(chave1 = 2, chave2 = 19, chave3=67)
d0 ["chave"] = '2'

# Modo mais usual
d1 ={"Chave1":"valor1"}
d1 ["Nova Chave"] = "valor"

# Chaves dentro do dicionário tem valores únicos. Quando uma chave repete inúmeras vezes o valor resultante dessa chave será o ultimo
d4 = dict(chave1 = 1,chave3 = 45, chave2 = 2);
print(d4)

# Qualquer valor imutável(strings,números e tuplas) pode ser utilizado como chaves.
d5={
    "chave1":12,
    13:"outro valor",
    (1,4,6):"",
}
print(d5)

# Para atualizar o valor de um dicionário utilizamos
d8={
    "chave1":12,
    13:"outro valor",
    (1,4,6):"",
}
d8 ["chave1"] = 17
print(d8);

# Para deletar o valor de uma chave utilizamos del
del d8[13]
print(d8)

# Para checar se existe uma chave dentro de um dicionário utilizamos:
print('chave1'in d8);

# Para checar se existe um valor dentro de um dicionário utilizamos:
print("" in d8.values())

# Para saber quantos dicionários existem dentro de uma variável usamos a função len
print(len(d8))

# Para iterarmos sobre os dicionários utilizamos
dicionario=dict(dicionario1=12, dicionario2=78, dicionario3=90, dicionario4=72)

for valor in dicionario.values(): # Iterando sobre valores
    print(valor)

print("################")

# Iterando sobre o conjunto chave valor.
for k,v in dicionario.items():
    print(k,v);

# Adicionando dicionários dentro de dicionários:
clientes={
    "cliente1":{
        "Nome":"Marcos Eduardo Fernandes",
        "Sobrenome":"Domingues",
        "Idade": 17,
        "Altura": 1.80
    },
    "Cliente2":{
        "Nome":"José Arnaldo",
        "Sobrenome":"Medeiros",
        "Idade": 70,
        "Altura": 1.80
    }    
}
# Iterando sobre dicionários dentro de dicionários
for clientes_k,clientes_v in clientes.items():
    print(f'Exibindo as chaves {clientes_k}');
    for dados_k,dados_i in clientes_v.items():
        print(f'\t{dados_k}={dados_i}');

# Para se fazer uma cópia rasa (Shallow Copy) de um dicionário utilizamos:
d12 = {1:'João',4.9:"Vinicius13",56:"pãoo"}
copia = d12.copy()
print(copia)
print("################")
# Para fazer uma cópia real de um dicionário utilizamos importações de módulo:
import copy
copia2 = copy.deepcopy(d12);
print(d12)
print(copia2)
print('######################################')
# Para fazer casting em dicionários utilizamos (funciona com listas e tuplas.)
lista = [ 
    ["lista1",231],
    ["lista2",884],
    ["lista3",15],
    ["lista4",34],
]
lista1 = dict(lista)
print(lista1)
print('######################################')

# Para remover um produto chave valor de um dicionário
print(lista1);
lista1.pop("lista1");
print(lista1);

# Para eliminar o ultimo item dentro de um dicionário utilizamos
lista1.popitem()
print(lista1);
print('######################################')
# Para concatenar dois dicionários utilizamos
d12.update(lista1);
print(d12);