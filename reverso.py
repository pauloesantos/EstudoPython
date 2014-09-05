def reverse(text):
    reverso = ""
    contador = len(text)
    r = range(len(text))
    for key in r:
        reverso += text[(len(text) - key) - 1]
    return reverso

print (reverse("calhanbeque"))
