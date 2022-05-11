perguntasRedes={
    "Primeira Pergunta":{
        "Pergunta":"Quanto é 1 + 3",
        "Resposta":{"A":4,"B":5,"C":7,"D":3,},
        "Resposta Correta": "A",
    },
    "Segunda Pergunta":{
        "Pergunta":"Quanto é 4 + 3",
        "Resposta":{"A":4,"B":5,"C":7,"D":3,},
        "Resposta Correta": "C"
    },
    "Terceira Pergunta":{
        "Pergunta":"Quanto é 2 + 3",
        "Resposta":{"A":4,"B":5,"C":7,"D":3,},
          "Resposta Correta": "B"
    },
}

respostasCertas = 0

for pk,pv in perguntasRedes.items():
    print(f'{pk},{pv["Pergunta"]}');
    print("Respostas")
    for rk, rv in pv['Resposta'].items():
        print(f'[{rk}]: {rv}');
    print()

    respostaUsuario = input("Digite a sua resposta ")

    if respostaUsuario == pv["Resposta Correta"]:
        print("Parabéns, você acertou a resposta!!!")
        respostasCertas += 1
        print()
    else:
        print("Que pena, você errou a resposta!!!")
        print()

print()
qtd_perguntas = len(perguntasRedes)
porcentagem_acerto = respostasCertas / qtd_perguntas *100
print(f'Você acertou {respostasCertas} questões')
print(f'Você acertou {porcentagem_acerto} das questões')
