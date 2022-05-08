"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada
"""

def funcao2():
    return "Olá mundo";


def funcao1(retornoFunc2):
    return retornoFunc2()

executando = funcao1(funcao2)
print(executando)
"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções que recebem um número diferente de argumentos. 
"""

def mestre(funcao,*args,**kyargs):
    return funcao(*args,**kyargs);

def fala_oi(nome):
    return f"Oi {nome}"

def saudacao(nome,saudacao):
    return f"{saudacao} {nome}"

execucao = mestre(fala_oi,'Marcos');
executando2 = mestre(saudacao,'Marcão', saudacao='Bom dia');
print(executando);
print(executando2);