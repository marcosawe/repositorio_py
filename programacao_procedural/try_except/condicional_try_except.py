# Tratando condicionais dentro de try except
def converte_numero(valor):
    try:
        valor =float(valor)
        return valor;
    except ValueError:
        try:
            valor=int(valor);
        except ValueError:
            pass

while True:
    numero = converte_numero(input("Digite um número"))
    if numero is None:
        print("Erro: Isso não é um número");
    else:
        print(numero * 2);
