# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:56:51 2020

@author: win10
"""

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
 


input_image = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\\thinning.jpg",0)



length,width=input_image.shape

comparison=np.ones((length,width),np.uint8)

comparison[147][109]=255;
comaparison1=comparison

kernel = np.array((
        [1, 1, 1],
        [1, 1,  1],
        [1, 1, 1]), dtype="int")

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

xl2 =np.ones((3,3))    


for var in range(1500):

    xl = cv2.dilate(comparison,kernel,iterations = 1)
    
    print(xl)
    print(xl2)
    if((var>0)&(np.array_equal(xl,xl2))):
        print("iguales")
        break
    
    xl2=xl
    
    
    comparison=andoperator(input_image,xl)
     

plt.subplot(111),plt.imshow(comparison, cmap = 'gray')
plt.title('conexion iteracion'+str(var)), plt.xticks([]), plt.yticks([])


