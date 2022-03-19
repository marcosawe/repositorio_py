"""
Enumerate - Enumerar elementos de uma lista #list
"""
lista = [
    ["Marcão", "Humilde", "Lindo", "Perfeito"],
    ["João", "Gordo", "Fodido", "Gay"],
    ["Maumau", "Desumilde", "Putinha do Marcoon", "Deveras Gay"],
        ]
for v1 in enumerate(lista):
    valor_enumerado, minhalista = v1
    print(minhalista)
