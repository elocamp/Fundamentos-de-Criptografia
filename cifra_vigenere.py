m = 'criptografia'
k = 'porta'

def cifra_vigenere(mensagem, chave):

    alfabeto = [] #algoritmo para gerar alfabeto
    for c in range(ord('a'), ord('z')+1):
        alfabeto = alfabeto + [chr(c).lower()]

    lista_m = []
    lista_k = []

    for e in m:
        x = alfabeto.index(e)
        lista_m.append(x)

    for f in k:
        y = alfabeto.index(f)
        lista_k.append(y)

    cont_m = 0
    cont_k = 0
    while cont_m < len(lista_m):
        lista_m[cont_m] = (lista_m[cont_m] + lista_k[cont_k]) % 26
        cont_m += 1
        cont_k += 1

        if cont_k >= len(lista_k):
            cont_k = 0

    for s in lista_m:
            print(alfabeto[s].upper(), end='')


cifra_vigenere(m, k)