Numero1 = input('Digite um número ')
Numero2 = input('Digite outro número ')
#isnumeric isdigit isdecimal
# Retona True a valores numéricos e positivos
try:
    Numero1 = float(Numero1);
    Numero2 = float(Numero2);
    print(Numero1 + Numero2);
except:
    print('Erro')