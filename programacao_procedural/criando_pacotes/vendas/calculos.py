# Calculos que serão importados 

from vendas.formata  import formatacao

def aumento_preco(preco,taxa,formata=False):
    r = preco + (preco * (taxa/100))
    if formata:
        return formatacao.real(r)
    else:
        return r

def reducao_preco(preco,taxa,formata = False):
    r = preco - (preco * (taxa/100))
    if formata:
        return formatacao.real(r)
    else:
        return r