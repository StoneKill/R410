from exo2 import decal_lettre

def vigenere(message: str, clef: str, chiffre: bool = True):
    message_sans_espace = '' # Suppression des espaces et de la ponctuation
    for char in message:
        if char.isalpha():
            message_sans_espace += char.lower()

    # Transformation de la clé en valeurs numériques (par rapport à 'a')
    clef_nmbr = []
    for char in clef:
        clef_nmbr.append(ord(char.lower()) - ord('a'))
    
    # Duplication de la clé pour correspondre à la longueur du message
    while len(clef_nmbr) < len(message):
        clef_nmbr = clef_nmbr + clef_nmbr

    message_crypt = ""
    for i, char in enumerate(message):
        shift = clef_nmbr[i] if chiffre else -clef_nmbr[i]
        message_crypt += decal_lettre(char, shift)

    return message_crypt

# Test
print(vigenere("Portez ce vieux whisky au juge blond qui fume", "Crypto", chiffre=True))
print(vigenere("VFRILHGKMITBFANZSZFIYPLGTITSTUQJPNYSV", "graphie", chiffre=False))

