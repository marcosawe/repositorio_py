import string


usuario = input('Nome do usuário ');
qtd_de_caractere = len(usuario);
if qtd_de_caractere <8:
    print('Você precisa digitar pelo menos 8 caractéres');

print (f'{usuario} possui {qtd_de_caractere} e pertence ao grupo dos {type(qtd_de_caractere)}');

string1 = input('Digite alguma coisa');
string2 = input('Digite outra coisa');
print(f'A quantiade de caractéres que foram ditos foi de {len(string1) + len(string2)}')