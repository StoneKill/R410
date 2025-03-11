def decal_lettre(lettre, x):
    
    if lettre.isalpha():
        return chr(ord(lettre) + (x%26))
    else:
        return lettre