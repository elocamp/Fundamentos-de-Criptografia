def BaconCipher(mensagem, mensagem_falsa):
    cod = [
        'aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab'
    ]
    cifra = []
    mf = []

    for i in mensagem:
        pos = ord(i) - 97
        cifra.append(cod[pos])

    for j in f:
        mf.append(j)

    strcifra = "".join(cifra)

    cont = 0
    while cont < len(strcifra):
        if ord(strcifra[cont]) == 98:
            mf[cont] = mf[cont].upper()
        cont += 1

    strmf = "".join(mf)


    print(strmf)
    print(strcifra)

m = input('Insira apenas com letras sem acentos e/ou espaços a mensagem a ser cifrada: ')
f = input('Insira apenas com letras sem acentos e/ou espaços a falsa mensagem: ')
if len(f) < len((5*m)):
    print('A mensagem falsa precisa ter o número de letras igual ou superior a 5x a mensagem original.')
else: BaconCipher(m, f)

#atacaraosul
#ascoisasmaismesquinhasenchemdeorgulhoosindividuosbaixos