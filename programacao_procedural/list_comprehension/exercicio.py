strings = '0123456789012345678901234567890123456789';
n = 10;
"""comp = [(i,i+n) for i in range(0, len(strings),n)];""" # Cria um conjunto de tuplas que determinan o início e o fim da iteração
comp = [strings[i:i+n] for i in range(0, len(strings),n)]; # Cria a iteração dentro do conjunto completo 
retorno = '.'.join(comp)
print(retorno);
