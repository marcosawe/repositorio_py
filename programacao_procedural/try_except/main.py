# É uma forma de tratar possíveis erros gerados no seu código, ou de criar excessões caso não possua respostas suficientes ou adequadas.

try:
    a = []
    print(a[1]);
except NameError as erro: # Quando tratamos de excessões precisamos informar o tipo de erro e envocalo em uma variável.
    print(f"Erro do corno do desenvolvedor, fale com ele");
except (IndexError,KeyError) as erro: # Erro de indice. # Para tratar mais de um erro por chave se utiliza tuplas ().
    print("Aconteceu um erro de index, ou chave valor!!!")
except Exception as erro: # Clausula que pega qualquer erro e executa o código pertencente a sua excessão.
    print("Aconteceu um erro inesperado...")
else: # Se nenhuma das informações for resolvida else executara a sua coluna de códigos.
    print("Sem erros meu consagra!!!")
finally:# É uma sintexe que sempre ocorre em qualquer tipo de circunstância de código.
    print("Sem erros meu consagra!!!")