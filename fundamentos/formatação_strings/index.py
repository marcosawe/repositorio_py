nome = 'Marcão';
idade = 17;
altura = 1.80;
e_maior = idade >= 18;
pesoM = 80;
imc = pesoM / (altura**2);

print(nome,' tem ', idade, 'e possui massa corporal de ', imc);
print(f'{nome} tem {idade} anos de idade, e seu imc é de {imc:.2f}');#Para ativar a formatação  de strings basta adicionar um f antes da string.
print('{} tem {} anos de idade, e seu imc é de {}'.format(nome, idade, imc));
#Outra forma de formatar strings