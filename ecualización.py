import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\laplaciano.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.equalizeHist(img)


im1 =cv2.imwrite("C:\\Users\win10\Desktop\procesamiento de imagenes\ecualización.jpg",img)


plt.imshow(img)
plt.axis('off')
plt.show()


cv2.imshow('Histogramas', img)
cv2.waitKey()