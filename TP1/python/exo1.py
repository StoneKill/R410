def PGCD(nb1: int, nb2: int):
    
    if nb1 <= 0 or nb2 <= 0: 
        # Si nb1 ou nb2 est negatif alors elle lève une erreur
        raise AttributeError('Les variables doivent être positive.')
    
    if (nb1 == nb2):
        # Si nb1 == nb2 alors elle retourne nb1
        return nb1
    
    if nb1 == 1 or nb2 == 1:
        # Si nb1 ou nb2 vaut 1 elle retourne 1
        return 1
    

    reste = nb1 % nb2
    print(f'{nb1} = {nb2} * {nb1//nb2} + {nb1%nb2}')
    if reste == 0:
        return nb2
    else:
        return PGCD(nb2, reste)
    


print(PGCD(16, 24))