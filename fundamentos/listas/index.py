########## Aplicações de Listas em Python ########

"""
Listas em phyton
fatiamento=[Inicio:Fim:Fatiamento];
append = Adiciona variáveis no final da lista; 
insert = Adiciona variáveis em qualquer local da lista;
pop = Deleta o último termo da lista;
del = Deleta qualquer termo da lista;
clear = 
extend = Concatena de forma interal os valores da lista;
+ = Concatena(Junta um conjunto) listas
min = Pega o valor mínimo da lista;
max = Pega o Valor máximo da lista;
range = Juntamente com a função list cria uma lista com os valores interáveis que são colocados na função range;
"""



################# Joguinho Básico Forca ############
palavra_secreta = "Hardware"
letras_digitadas= []
chances = 3
while True:
    if chances <= 0:
        print("Você perdeu !!!")
        break

    letra = input("Digite uma letra: ");
    
    if len(letra) != 1:
        print("Digite somente uma letra!");
        continue
    
    letras_digitadas.append(letra);

    if letra in palavra_secreta:
        print(f'A letra {letra} existe na palavra secreta');

    else:
        print(f'A letra {letra} não existe na palavra');
        letras_digitadas.pop()
    print(letras_digitadas)
    
    secreto_temporario = ""
    for letras_secreta in palavra_secreta:
        if letras_secreta in letras_digitadas:
            secreto_temporario += letras_secreta
        else:
            secreto_temporario +='*'

    if secreto_temporario == palavra_secreta:
        print(f"Você Ganhou !!! A palavra era {palavra_secreta}.")
        break
    else:
        print(f'A palavra temporária está assim {secreto_temporario}')
    if letra not in palavra_secreta:
        chances -= 1
    
    print(f'Você ainda tem {chances} chances.')
    print()
    
