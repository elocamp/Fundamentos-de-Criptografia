#Algoritmo que recebe um texto plano (apenas letras) e desloca seus elementos em uma chave k

def cifra_deslocamento(m, k):
    lista = []
    lista1 = []
    letras = True


    for e in m:

        if 32 <= ord(e) <= 64 or 91 <= ord(e) <= 96 or 123 <= ord(e) <= 126: #Caso o caractere esteja fora desse range ele automaticamente não é uma letra
            letras = False


        if 65 <= ord(e) <= 90:
            lista.append(ord(e) + k + 32) #Caso a letra seja maiúscula, ele a adiciona na lista como minúscula, que no unicode é o código dela própria + 32

        if 97 <= ord(e) <= 122:
            lista.append(ord(e) + k)     #Caso a letra já seja minúscula, ela é adicionada à lista normalmente


    if letras == False:
        print('A entrada está inválida. Apenas letras são aceitas.')

    for j in lista:

        if j > 122:
            r = j - 122
            j = 96 + r    #Caso a letra ultrapasse o range máximo, que encerra no 'z', ela recomeça o ciclo a partir do 'a'

        if j < 97:
            r = (j - 97) * -1
            j = 123 - r  #O mesmo acontece no inverso, caso ela ultrapasse o range mínimo, que encerra no 'a', ela recomeça o ciclo a partir do 'z'

        lista1.append(chr(j))

    for q in lista1:
        print(q, end='')

cifra_deslocamento('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)

cifra_deslocamento('ABCDEFGHIJKLMNOPQRSTUVWXYZ', -1)

cifra_deslocamento('T1E2S3T4E5', 0)