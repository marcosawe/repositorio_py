# Escopo Global
variavel = 'Valor';

# Imprime a variavel de escopo global 'Valor'
def func():
    print(variavel);

func()

# Imprime a variável dentro do escopo
def func2():
    variavel = 'Outro Valor!!!';
    print(variavel);

func2();
print(variavel);

# Forma ideal para tonar global a variável dentro de um escopo
def func3(args=None):
    arg = args.replace("V","c")
    return(arg)

outra_variavel = func3(args=variavel)
print(outra_variavel)