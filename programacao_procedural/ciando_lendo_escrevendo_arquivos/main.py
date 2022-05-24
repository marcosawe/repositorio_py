# Para abrirmos um arquivo, utilizamos o nome do arquivo e a função que será executada nele.

file = open('Peba.txt','w+') # Abrindo o arquivo.
file.write(f"Linha 1 \n") # Escrevendo no arquivo.
file.write(f"Linha 2 \n")
file.write(f"Linha 3 \n")
file.write(f"Linha 4 \n")
file.close() # Fechando o arquivo.

# Sempre que abrir um arquivo feche o mesmo para fazer outra operação.

# Se caso você não tenha fechado a função e precisa voltar o cursor ao ponto de origem utilizasse seek.

file2 = open('Pimba.txt','w+') 
file2.write(f"Linha 1 \n")
file2.write(f"Linha 2 \n")
file2.write(f"Linha 3 \n")
file2.write(f"Linha 4 \n")
file2.seek(0,0)

# Para lermos as linhas do arquivo utilizamos
print(file2.read())
file2.close()

# Para apagarmos um arquivo utilizamos 
import os
os.remove('Peba.txt')
os.remove('Pimba.txt')

# Para transformar um arquivo de texto em json utilizamos

import json # Importe o módulo do Json

d1={
    "pessoa1":{
        "nome":"Carlos",
        "idade":22, 
        "apelido":"Carlão do Pastel", 
        "signo":"Touro",    
    },
    "pessoa2":{
        "nome":"Marcos",
        "idade":19, 
        "apelido":"Marcão do Birinbal", 
        "signo":"Touro",    
    },
}


# O método indent identa a operação
d_json = json.dumps(d1, indent=True) # Transforma o dicionário em Json
print(d_json)