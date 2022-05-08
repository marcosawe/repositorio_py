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

for k in dicionario.items():
    print(k);