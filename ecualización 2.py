
import cv2
import numpy
from PIL import Image
import matplotlib.pyplot as plt
 
img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\exponencial.jpg")
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)


