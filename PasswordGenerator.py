import random
minusculas = "abcdefghiklmn"
mayusculas = "ABCDEFGHIJKL"
numeros = "123456789"
respuesta = ""
app = input ("¿para qué APP desea usted la contraseña? ")
for x in range(0,4):
    respuesta = respuesta + random.choice(minusculas) + random.choice(mayusculas) + random.choice(numeros)
print ( "su contraseña para  "+ app +" es " + respuesta)