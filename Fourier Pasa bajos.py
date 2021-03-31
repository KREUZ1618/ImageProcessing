import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\V6.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# Crea la máscara primero, el centro del cuadrado vale 1, el resto son ceros
mask = np.zeros((rows,cols),np.uint8)
grado=5;

mask[crow-60:crow+60, ccol-60:ccol+60] = 1

# Aplica la máscara y la DFT inversa
fshift = fshift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(20*np.log(np.abs(fshift)), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])
