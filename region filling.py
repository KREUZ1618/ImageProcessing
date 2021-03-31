# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:06:25 2020

@author: win10
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:58:23 2020

@author: win10
"""

# for inline image display inside notebook
# % matplotlib inline
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io   import imread, imsave, imshow, show, imread_collection
from skimage.io import imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc
import cv2
import numpy as np
 


input_image = np.array((
    [255, 255, 255, 255, 255, 255, 255, 255],
    [255, 0, 0, 0, 0, 0, 255, 255],
    [255, 0, 0, 0, 0, 0, 255, 0],
    [255, 255, 255, 255, 255, 255, 255, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0,255, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]), dtype="uint8")

comparison = np.array((
    [0, 0, 0, 0, 0, 0,0, 0],
    [0, 255, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0,0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]), dtype="uint8")




kernel = np.array((
        [-1, 1, -1],
        [1, 1,  1],
        [-1, 1, -1]), dtype="int")

def andoperator(array,array2):
    
    length,width=array.shape
    
    print(array.shape)
    
    array3=np.ones((length,width))
    
    for w in  range(0,width):
        for l in range(0,length):
                   
            if((array[w][l]==255)&(array2[w][l]==255)):
                array3[w][l]=255
            else:
                array3[w][l]=0
    
    return array3
            
        
my_dpi=120

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

xl2 =np.ones((8,8))    


for var in range(10):

    xl = cv2.dilate(comparison,kernel,iterations = 1)
    
    print(xl)
    print(xl2)
    if((var>0)&(np.array_equal(xl,xl2))):
        print("iguales")
        break
    
    xl2=xl
    
    
    comparison=andoperator(cv2.bitwise_not(input_image),xl)
     
    
    



    


plt.subplot(141),plt.imshow(kernel, cmap = 'gray')
plt.title('kernel'), plt.xticks([]), plt.yticks([])

 
plt.subplot(142),plt.imshow(input_image, cmap = 'gray')  
plt.title('original'), plt.xticks([]), plt.yticks([])
  
plt.subplot(143),plt.imshow(cv2.bitwise_not(input_image), cmap = 'gray')
plt.title('complemento'), plt.xticks([]), plt.yticks([])


plt.subplot(144),plt.imshow(comparison, cmap = 'gray')
plt.title('relleno iteracion'+str(var)), plt.xticks([]), plt.yticks([])






