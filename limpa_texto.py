#Algoritmo limpador de texto, atendendo a atividade 1 para o dia 27/08/2020

def limpa_texto(m):
    lista = []

    for i in m:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:    #65 a 90 compreende todas as letras maiúsculas no unicode, enquanto 97 a 122 compreende todas as minúsculas
            lista.append(i.lower())

    for j in lista:
        print(j, end='')
        
limpa_texto('EnTrAdA1273856784964&#$%&##¨@#  dE$%¨#$%t&E%s)T*e')