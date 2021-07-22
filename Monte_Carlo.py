import random

lar_retangulo = 1000
alt_retangulo = 1000

a = 100
b = 900
Gxi = 100
Fxi = 900

cont = 0
lista_x = []
while cont < 25000:
    ponto_x = random.randrange(0, 1000)
    if a < ponto_x < b:
        lista_x.append(ponto_x)
    cont += 1

cont1 = 0
lista_y = []
while cont1 < 25000:
    ponto_y = random.randrange(0, 1000)
    if Gxi < ponto_y < Fxi:
        lista_y.append(ponto_y)
    cont1 += 1

A_ret = lar_retangulo * alt_retangulo
N_dentro = len(lista_x) + len(lista_y)
N_total = 25000*2

print("A área do retângulo é = %0.3f m² " %A_ret)
A_rio = (N_dentro/N_total) * A_ret
print("A área do rio é = %0.3f m²" %A_rio)


