import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\V6.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
print(img.shape)
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-10:crow+10, ccol-10:ccol+10] = 0
print(fshift)
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(np.abs(fshift), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back,cmap = 'gray')
plt.title('Transformada inversa'), plt.xticks([]), plt.yticks([])
plt.show()