# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:05:07 2020

@author: win10
"""

from PIL import Image
import math as m
import numpy as np
import matplotlib.pyplot as plt



def histograma(imagen):
    
    im = imagen
    m = im.size[0]      #Filas
    n = im.size[1]      #Columnas
    l = 256            #Profundidad de la imagen
    h = np.zeros(l)     #Crea el vector del histograma inicializado en ceros
    
    #Ingresa los valores al histograma
    i = 0
    while i < m:
        j = 0
        while j < n:
            h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
            j+=1
        i+=1
    return h



def graficar(datos, nombre_del_archivo):
   
    plt.plot(datos)
    x=range(len(datos))
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title(nombre_del_archivo)
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.show()

    return None


"""ESTIRAMIENTO DE CONTRASTE"""
def contraste(imagen,constante):
    ima = Image.open(imagen)
    im = ima.convert('L')
    im.show()
    m = im.size[0]           #Filas
    n = im.size[1]           #Columnas
    l = 256                  #Profundidad de la imagen
    h1 = histograma(im)      #Crea el vector del histograma original
    graficar(h1,"Histograma Original")       #Grafica histograma original
    
    img = np.array(im)      #Arreglo de la imagen
    
    Im = 0                  #Valor mínimo permitido
    IM = 255                #Valor máximo permitido
    Vm = 50       #Valor mínimo del rango
    VM = 200        #Valor máximo del rango
    
    f = (IM-Im-constante)/(VM-Vm)
    
    im2 = Image.new('L',(m, n), "white")   #Creación de nueva imagen
    
    #Mapeo
    i = 0
    while i < m:
        j = 0
        while j < n:
            if (im.getpixel((i,j))) < Vm:
                im2.putpixel((i,j),0)
            elif (im.getpixel((i,j))) > VM:
                im2.putpixel((i,j),255)
            else:
                im2.putpixel((i,j),(int(round(f*(im.getpixel((i,j))-Vm)+1))))
            j+=1
        i+=1
    im2.show()
    im2.save("i9.jpg")
    h2 = histograma(im2)       #Crea el vector del histograma original
    graficar(h2,"Histograma del estiramiento de contraste")       #Grafica histograma original
    return im2
      
imagen1=contraste("C:\\Users\win10\Desktop\procesamiento de imagenes\P4.jpg",0)
imagen1=imagen1.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\Edecontraste.jpg")

    
