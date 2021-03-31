import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\V6.jpg",0)

f = np.fft.fft2(img)
"""nos proporciona la transformación de frecuencia, la cual será una matriz compleja. 
Su primer argumento es la imagen de entrada,que deberá estar en escala de grises. El segundo argumento es opcional y decide el tamaño de la matriz de salida.
Si es mayor que el tamaño de la imagen de entrada, la imagen de entrada se rellena con ceros antes del cálculo de FFT. Si es inferior a la imagen de entrada,
se recortará la imagen de entrada.Si no se pasa ningún argumento, el tamaño de la matriz de salida será igual al de la entrada."""
fshift = np.fft.fftshift(f)
"""
Una vez obtenido el resultado, la componente de frecuencia cero (componente DC) estará en la esquina superior izquierda. Si quieres ponerlo en el centro, necesitas desplazar el resultado en N/2 en ambas direcciones. 
Esto se hace simplemente con la función np.fft.fftshift(f)
"""
magnitudFFT =20*np.log(np.abs(fshift))
#normalización 


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitudFFT, cmap = 'gray')
plt.title('FFT'), plt.xticks([]), plt.yticks([])
plt.show()

