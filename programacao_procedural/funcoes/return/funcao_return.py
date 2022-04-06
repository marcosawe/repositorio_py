'''
Funções(def) em python -> return
'''
#Não se utiliza funções para imprimir valores em python. Elas são utilizadas para retornar tratamentos dentro de uma variável.

def funcao(var):
    return var

variavel = funcao("")
print(variavel) #None também é um tipo de valor em phyton (não valor)

if variavel:
    print(variavel);
else:
    print("Nenhum Valor")

# Utilizando estruturas condicionais com função

'''print('Vamos executar a divisão de números')
def divisao(n1,n2):
    if n2==0:
        return
    else:
        return n1/n2

divide = divisao(6,7)

if divide:
    print(divide)
else:
    print('O valor não é divisível!')'''
