from hashlib import sha256
from binascii import unhexlify


def inverse_modulo(a, m):
  try:
    for x in range(1, m):
        if (a % m) * (x % m) % m == 1:
            return x
  except: 
     Exception("The modular inverse does not exist.")
  
