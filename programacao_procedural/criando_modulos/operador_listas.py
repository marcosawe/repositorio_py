# É utilizado para organizar as funções criadas pelo programador por cada área de atuação

# Cófigos do módulo
import math
PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]


def divide_lista(Lista,y):
    return [x/y for x in Lista];

# Para não propagar os teste para outros módulos utilizamos:
if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9]
    print(divide_lista(lista,4))
    print(dobra_lista(lista))
    print(PI)