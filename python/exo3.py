from exo2 import decal_lettre

def vigenere(message: str, clef: str, chiffre: bool = True):
    # Duplication de clef jusqu'a ce qu'on ait assez de longueur de clé
    while len(clef) < len(message):
        clef = clef + clef

    # Transfo des chars de la clé en val ASCII
    clef_nmbr = list()
    for char in clef:
        clef_nmbr.append(ord(char))


    # Décalage de chaque lettre du msg avec la lettre équivalente de la clef
    message_crypt = str()
    if chiffre:
        for i in range(len(message)):
            message_crypt += decal_lettre(message[i], clef_nmbr[i])
    else:
        for i in range(len(message)):
            message_crypt += decal_lettre(message[i], -clef_nmbr[i])
    return message_crypt


print(decal_lettre('a', ord("A")))
#print(vigenere("Portez ce vieux whisky au juge blond qui fume", "Crypto", chiffre = True))

