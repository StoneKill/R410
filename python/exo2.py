def decal_lettre(lettre: str, x: int):
    # Si lettre n'est pas une lettre, on renvoit la lettre tel quel
    if not lettre.isalpha():
        return lettre
    

    if lettre.isupper():
        # Vu que ord(A) = 65, pour normaliser on fait - 65
        lettre_norm = ord(lettre) - 65

        # On fait le décalage, on modulo 26 pour rester dans l'alphabet, on dénormalise et on retransforme en char
        return chr(((lettre_norm + x) % 26) + 65)
    else:
        # Vu que ord(A) = 65, pour normaliser on fait - 97
        lettre_norm = ord(lettre) - 97
        
        # On fait le décalage, on modulo 26 pour rester dans l'alphabet, on dénormalise et on retransforme en char
        return chr(((lettre_norm + x) % 26)+ 97) 




def chiffre_cesar(message: str, decalage: int, chiffre: bool=True):
    newChaine = str()

    if chiffre:
        for char in message:
            newChaine += decal_lettre(char, decalage)
        return newChaine
    else:
        for char in message:
            newChaine += decal_lettre(char, -decalage)
        return newChaine

def bruteForce_Caesar(message):
    pass 