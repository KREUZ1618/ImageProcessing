

from PIL import Image
import numpy as np
#modulo para generar el histograma 
import matplotlib.pyplot as plt


def graficar(datos, nombre_del_archivo):
   
    plt.show(nombre_del_archivo)
    x=range(len(datos))
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title('Histograma')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    

    return None


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


foto=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\P4.jpg")

plt.imshow(foto)
plt.axis('off')
plt.show()

if foto.mode != 'L':
    foto=foto.convert('L')

h=histograma(foto)

graficar(h,"histograma")
