from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta=FileDialog.askopenfilename(initialdir='.', filetype=(("Ficheros de texto","*.txt"),),title="Abrir un fichero de texto")
archivo=open(ruta,"r")
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
print("El archivo tiene: ",lineas," lineas, ",numPalabras," palabras y",numLetras, " letras")