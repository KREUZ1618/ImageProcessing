

from PIL import Image
import math as m
import numpy as np
import matplotlib.pyplot as plt



def histograma(imagen):
    
    im = imagen
    alto = im.size[0]      #Filas
    ancho = im.size[1]      #Columnas
    l = 256            #Profundidad de la imagen
    h = np.zeros(l)     #Crea el vector del histograma inicializado en ceros
    
    #Ingresa los valores al histograma
    i=0
    for i in range(0,alto):
        j=0
        for j in range(0,ancho):
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




def umbralfuerte(imagen,threshold):
    ima = Image.open(imagen)
    im = ima.convert('L')
    im.show()
    t = threshold
    alto = im.size[0]           #Filas
    ancho = im.size[1]           #Columnas
    l = 256                  #Profundidad de la imagen
    h1 = histograma(im)      #Crea el vector del histograma original
    graficar(h1,"Histograma Original")     #Grafica histograma original
    
    im2 = Image.new('L', (alto, ancho), "white")   #Creación de nueva imagen
    
    #Mapeo
    i = 0
    for i in range(0,alto):
        j=0
        for j in range(0,ancho):
            if (im.getpixel((i,j))) <= t:
                im2.putpixel((i,j),0)
            else:
                im2.putpixel((i,j),(im.getpixel((i,j))))
            j+=1
        i+=1
    im2.show()
    
    h2 = histograma(im2)       #Crea el vector del histograma original
    graficar(h2,"Histograma del umbral fuerte")       #Grafica histograma original
    return im2



imagen1=umbralfuerte("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",150)
imagen1=imagen1.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\fuerte.jpg")

