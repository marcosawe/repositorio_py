nome = input('Qual seu nome?');
idade = input('Qual a sua idade?');
ano_nascimento = 2022 - int(idade);
print();
print(f'O usuário digitou {nome}, e o tipo da variável é',type(nome));
print();
print(f'Meu nome é {nome} e minha idade é {idade}');
print(ano_nascimento)