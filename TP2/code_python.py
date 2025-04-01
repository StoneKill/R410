from random import *
from exo1_copie import PGCD
from fonction_RSA import inverse_modulo

def crible_eratosthene(n: int) -> list[int]:
    liste = [True] * (n+1)
    liste[0],liste[1] = False, False # 0 et 1 sont premier
    
    for i in range(2,n): # On parcourt la liste à partir de 2 car 0 et 1 sont premier
        j = i+i # On fait les multiples de i
        while j < len(liste): # Tant que j est dans la liste
            liste[j] = False # On dit que j (multiple de i) n'est pas 1er
            j += i # Et on fait le prochain multiple de i
    
    vraie_liste = []

    for i in range(len(liste)):
        if liste[i]:
            vraie_liste.append(i) # On transforme notre liste de bool en liste de nmbr

    return vraie_liste




# Exemple d'utilisation :
# print(crible_eratosthene(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


M = 42 # Message
D = 107 # L'exposant privé
N = 187 # Modulo

S = (M**D)%N

E = 3 # Exposant public

'''if __name__ == "__main__":
    print(f'La signature : {(S**E)%N}')
    print(f'Le message : {M}')
    print(f'Donc la vérification = {(S**E)%N == M}')
'''

def signer_rsa(message:int, expo_pub:int, modulo: int) -> int:
    return (message**expo_pub)%modulo

def signature_rsa_est_valide(message:int, signature, expo_pub:int, modulo:int):
    return message == (signature**expo_pub)%modulo

# print(signature_rsa_est_valide(42,70,3,187))
# print(signature_rsa_est_valide(45,70,3,187))

def generer_clef_rsa():
    nb_premier = crible_eratosthene(100)  
    p, q = choice(nb_premier), choice(nb_premier)

    
    while p == q:
        q = choice(nb_premier)
    
    N = p * q  # Modulo N
    phi_N = (p - 1) * (q - 1)  # Euler's totient function
    
    # Choose a public exponent e
    e = 3  # Typically 3 or 65537
    while e >= phi_N or PGCD(e, phi_N) != 1:
        e = choice([3, 5, 17, 257, 65537])  # Ensure e is coprime with φ(N)
    
    # Compute the private exponent d
    d = inverse_modulo(e, phi_N)  # d is the modular inverse of e modulo φ(N)

    print(f"Public Key: (e={e}, N={N})")
    print(f"Private Key: (d={d}, N={N})")
    
    return (e, N), (d, N)  # Return the public and private keys
    

generer_clef_rsa()