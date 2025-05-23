def decal_lettre(lettre: str, x: int):
    # Si lettre n'est pas une lettre, on renvoit la lettre tel quel
    if not lettre.isalpha():
        return lettre


    if 65 <= ord(lettre) <= 90: # Si majuscule
        return chr(((ord(lettre)-65 + (x%26)) %26)+ 65)
    else: # Sinon (minuscule)
        return chr(((ord(lettre)-97 + (x%26)) %26)+ 97)




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


def bruteForce_Caesar(message: str):
    for i in range(25):
        print(chiffre_cesar(message, i, False))



def attaqueCaeser_stat(filename: str):
    lettre_freq = dict()
    with open(filename, 'r') as f:
        content = f.read()
    for char in content:
        if char.isalpha():
            if char in lettre_freq:
                lettre_freq[char] += 1
            else:
                lettre_freq[char] = 1
    
    cle_max = list(lettre_freq.keys())[0]
    val_max = list(lettre_freq.values())[0]
    for cle, val, in lettre_freq.items():
        if val > val_max:
            val_max = val
            cle_max = cle


    with open(f"{filename}_{ord(cle_max) - ord('e')}_decrypted.txt", 'w') as F:
        F.write(chiffre_cesar(content, ord(cle_max) - ord('e'), False))

# attaqueCaeser_stat('/home/adminetu/Bureau/TPCrypto_DEGRAY/caesar_encrypted.txt')