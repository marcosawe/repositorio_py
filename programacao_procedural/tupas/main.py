"""
Funcionam como listas porém não podem ser alteradas.
"""
# Para se criar tuplas utilizamos:
from tkinter import N


t1 = (1,'',3,"Jorge",'mkdir')
t2 = 2,4,6,'João','rm -r'
t3 = 3,
print(type(t3))
# Para acessar o indice de uma tupla utilizamos
print(t2[3])
# Para iterar sobre uma tupla utilizamos 
for vp in t2:
    print(vp)

# Para fatiar sobre uma tupla utilizamos
print(t1[2:])

# Para desempacotar as tuplas utilizamos
n1,n2,*n = t2
print(*n)

# Para transformar tuplas em listas e vice-versa utilizamos
print(type(t2))
t2 = list(t2)
print(type(t2))
t2 = tuple(t2)
print(type(t2))