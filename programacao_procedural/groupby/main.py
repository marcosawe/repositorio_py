# Agrupando elementos dentro de um dicionário em python

alunos= [
    {'Nome':'João','Nota':'A'},
    {'Nome':'Júlia','Nota':'B'},
    {'Nome':'José','Nota':'D'},
    {'Nome':'Carlos','Nota':'C'},
    {'Nome':'Felipe','Nota':'A'},
    {'Nome':'Marcos','Nota':'B'},
    {'Nome':'Marina','Nota':'A'},
];
# Ordenando a lista por nota:
from itertools import groupby,tee

ordena = lambda item:item['Nota'] # expressão lambda 
alunos.sort(key= ordena);
alunos_agrupados = groupby(alunos,ordena) # A função group precisa da lista setada em uma variável e uma espressão lambda com um keyarg para requerir um valor de dicionário dentro da lista 

for agrupamento, elementos_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}');
    for alunos in elementos_agrupados:
        print(f'Alunos:{alunos}');
        print()

# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
  v1, v2 = tee(valores_agrupados)

  print(f'Agrupamento: {agrupamento}')

  for aluno in v1:
    print(f'\t{aluno}')

  quantidade = len(list(v2))
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')