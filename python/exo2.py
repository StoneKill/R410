def decal_lettre(lettre, x):
        return chr(ord(lettre) + (x%26))

print(decal_lettre('A', 256))
