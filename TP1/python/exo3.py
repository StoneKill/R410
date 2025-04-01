from exo2 import decal_lettre

def vigenere(message: str, clef: str, chiffre: bool = True):
    message_sans_espace = '' # Suppression des espaces et de la ponctuation
    for char in message:
        if char.isalpha():
            message_sans_espace += char.upper()

    # Transformation de la clé en valeurs numériques (par rapport à 'a')
    clef_nmbr = []
    for char in clef:
        clef_nmbr.append(ord(char.upper()) - ord('A'))
  
    # Duplication de la clé pour correspondre à la longueur du message
    while len(clef_nmbr) < len(message_sans_espace):
        clef_nmbr = clef_nmbr + clef_nmbr

    message_crypt = ""
    # Cette ligne nous permet d'avoir un parcours par elem tout en ayant un indice
    for i, char in enumerate(message_sans_espace):
        decalage = clef_nmbr[i] if chiffre else -clef_nmbr[i]
        message_crypt += decal_lettre(char, decalage)
    
    return message_crypt

# Test
#print(vigenere("Portez ce vieux whisky au juge blond qui fume", "Crypto", chiffre=True))
#print(vigenere("VFRILHGKMITBFANZSZFIYPLGTITSTUQJPNYSV", "graphie", chiffre=False))


# La partie attaque étant BIEN TROP COMPLIQUE, je ne peux pas la faire sans tricher. Désolé.