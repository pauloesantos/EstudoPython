def median(lista):
    lista = sorted(lista)
    print (lista)
    contador = len(lista)
    if len(lista) % 2 != 0:
        return lista[contador / 2]
    else:
        x = int(contador / 2)
        firstElem = lista[x]
        print (firstElem)
        secondElem = lista[x - 1]
        print (secondElem)
        return (firstElem + secondElem) / 2

print(median([4, 5, 5, 4]))
