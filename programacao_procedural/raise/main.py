# É Um método que levanta funções, para tratar excessões dentro de python
#Forma de levanatr raise em funções
def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print("Log: ",error)
        raise


print(divide(30,0))

# Forma de levantar raise com if else
def divide2(n1,n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0")
    return n1/n2


print("################################################")
