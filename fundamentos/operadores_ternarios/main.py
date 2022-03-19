"""
Operadores Ternários em Phyton - Facilita a atribuição de if else por meio de uma variável que será enterpretada
"""
"""
Em vez de se fazer:

    logged_user = True
        if logged_user == True
            msg ="Usuário Logado"
        else
            msg ="Usuário não está logado"
    
    print(msg)
Utilizamos:
"""

logged_user = False
msg = "Usuário Logado" if logged_user else "Usuário precisa logar "
print(msg)
#####################################################
idade = input("Qual é a sua idade? ")
if not idade.isnumeric:
    print("Você precisa digitar apenas números")
else:
    idade = int(idade)
    maior_idade = (idade>=18)
    msg = "Pode acessar o site" if maior_idade else "Usuário precisa ter mais de 18 anos."

print(msg)