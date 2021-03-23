##leia da entrada padrão nomes completos, compostos de nome e sobrenome(s), de pessoas até que uma string vazia seja lida
##2 defs + pgm principal


def ordena(razao):
    for indice1 in range(len(razao)):
        var = indice1
        for indice2 in range(len(razao)):
            if razao[indice1] < razao[indice2]:
                temp = razao[indice1]
                razao[indice1] = razao[indice2]

                razao[indice2] = temp

    return razao


def repetidos(resultado):
    contados = set()
    contador = 0
    for indice in range(len(resultado)):
        for valor in resultado[indice:]:
            if valor  == resultado[indice]:
                contador += 1
        if len(resultado[indice]) > 2 and contador > 1:
            contados.add(resultado[indice])
        contador = 0
    contados = list(contados)

    return ordena(contados)


##programa principal
entrada = -1
lista = []
while True:
    if not entrada:
        break
    entrada = input('Digite o nome: ').split()  ## leia da entrada padrão nomes completos, compostos de nome e sobrenome
    lista.extend(entrada)
lista = repetidos(lista)

for valores in lista:

    print("nome repetido:  "+valores)