"""
funções -> def em phyton
"""
from ssl import ALERT_DESCRIPTION_BAD_RECORD_MAC


def funcao(valor):
    print(f"Olá {valor} mundo!!!")

funcao('Mamaco') 

# Para definir um valor padrão para uma função utilizamos:
def valor(primata = 'mamaco'):
    primata = primata.replace('a','i');
    print(f'Saudações {primata}');
    return f'{valor}'

variavel = valor()
print(variavel)