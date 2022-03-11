#    indices
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de Roma'; #Iterável
tamanho_frase = len(frase);
contador = 0;
nova_string = '';
input_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador];
    if letra == input_usuario:
        nova_string += input_usuario.upper();
    else:
        nova_string += letra;
    contador += 1;

print(nova_string);
    
    
    
    #nova_string += frase[contador];
    #print(nova_string);
    #contador += 1;
    #print(frase[contador],contador);