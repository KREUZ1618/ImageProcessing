

from skimage import img_as_float
from skimage import io, color, morphology
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


th,image_binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

print(image_binary)

image_binary=img_as_float(image_binary)

out_skeletonize = morphology.skeletonize(image_binary)

out_thin = morphology.thin(image_binary)

my_dpi=120

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

plt.subplot(121),plt.imshow(image_binary, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


plt.subplot(122),plt.imshow(out_skeletonize, cmap = 'gray')
plt.title('skeleton'), plt.xticks([]), plt.yticks([])



