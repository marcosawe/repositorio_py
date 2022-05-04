'''
Funções (def) em python - *args  **keywords 
'''
def func(ag1,ag2,ag3= 7, ag4=8): # A partir do momento que é setado um valor padrão ao argumento eu preciso setar aos demais argumentos entegrados. 
    print(ag1,ag2,ag3,ag4);

func(1,2,10)

# Argumentos *args (Utilizado para definir um conjunto de argumentos até então desconhecidos)
def funcao(*args):
    print(*args)

lista = []