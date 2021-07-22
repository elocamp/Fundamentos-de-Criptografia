#Algoritmo que recebe um texto plano e desloca seus elementos em uma chave k

def cifra_deslocamento(m, k):
    lista = []
    lista1 = []

    for e in m:

        if 65 <= ord(e) <= 90:
            lista.append(ord(e) + 32) #Caso a letra seja maiúscula, ele a adiciona na lista como minúscula, que no unicode é o código dela própria + 32

        if 97 <= ord(e) <= 122:
            lista.append(ord(e))     #Caso a letra já seja minúscula, ela é adicionada à lista normalmente

        if 32 <= ord(e) <= 64 or 91 <= ord(e) <= 96 or 123 <= ord(e) <= 126:   #Unicode dos caracteres especiais e números
            lista.append(ord(e))

    for j in lista:

        if 97 <= j <= 122:
            j += k

            if j > 122: #Caso a letra ultrapasse o range máximo, que encerra no 'z', ela recomeça o ciclo a partir do 'a'
                r = j - 122
                j = 96 + r

            if j < 97:
                r = (j - 97) * -1
                j = 123 - r #O mesmo acontece no inverso, caso ela ultrapasse o range mínimo, que encerra no 'a', ela recomeça o ciclo a partir do 'z'


        lista1.append(chr(j))

    for q in lista1:
        print(q, end='')


cifra_deslocamento('ABC123 -*/%$# 321bca', 1)

cifra_deslocamento('Rua Maria Severina da Costa, 354', 3)