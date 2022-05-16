# Valores Iteraveis.
# São valores que você pode iterar sobre eles mas não necessariamente ele é um iterador.
lista = [0,1,2,3,4,5,6,7,8,9]

#  Iteradores
# É a função que dá um valor de cada vez
lista = [0,1,2,3,4,5,6,7,8,9]
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# Geradores são utilizados para reduzir a quantidade de tempo e processamento sobre alguma iteração
import time
import sys

lista = list(range(10000))
print(sys.getsizeof(lista))

def gera():
    r=[]
    for n in range(0,100):
        yield n # Lazy avaliation(Não espera todos os dados serem processados para printar o número da tela.)
        time.sleep(0.1)
    return r

g = gera()

for v in g:
    print(v)