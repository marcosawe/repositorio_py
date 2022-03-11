"""
Manipulando strings - aula 6 
* Sting indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in, len, abs, type, print, etc.
Essas funções podem ser usadas diretamente em cada tipo. 
"""
# Positivos
#       [012345678]
texto = 'Python S2'
print(texto[4]);
Nova_String = texto[2:6];
print(Nova_String)

# Negativos
#      -[987654321]  
texto = 'Python 2S'
print(texto[-5:-1]);

# Utilizando Step
print(texto[0:8:2])