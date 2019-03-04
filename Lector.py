from io import open

archivo=open("Archivo.txt","r")
texto =archivo.readlines()
archivo.close()
lineas=len(texto)
numPalabras=0
numLetras=0;
palabras=[]
for i in texto:
    palabras+=i.split()
for i in palabras:
    numLetras+=len(i)
numPalabras+=len(palabras)
print("El archivo tiene: ",lineas," líneas, ",numPalabras," palabras y",numLetras, " letras")