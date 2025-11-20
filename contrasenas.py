import string
import random

#Input de la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

#Tipos de caracteres a incluir en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

#Generación de la contraseña
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

#Mostrar la contraseña generada
print("La contraseña es :" + contrasena)
