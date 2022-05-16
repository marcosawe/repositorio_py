# Faça a soma de todos os valores dos produtos dentro de uma list comprehension

carrinho = []
carrinho.append(('produto1',30))
carrinho.append(('produto2',32))
carrinho.append(('produto3',40.93))
carrinho.append(('produto4',10))
print(carrinho)

total=sum([float(y) for x,y in carrinho])
print(total)