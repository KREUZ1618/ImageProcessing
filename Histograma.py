# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:21:08 2020

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
def Histograma(im,n,w,v,t):
    H=np.zeros(shape=(3,256))
    for i in range(0,w):
        for j in range (0,v):
            for k in range(0,t):
                H[i,int(round(im[j,k,i]))]=H[i,int(round(im[j,k,i]))]+1
    if(n==0):
        plt.plot(H[0])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de rojos original")
        plt.grid()
        plt.show()
        
        plt.plot(H[1])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de verdes original")
        plt.grid()
        plt.show()
        
        plt.plot(H[2])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de azules original")
        plt.grid()
        plt.show()
    if(n==1):
        plt.plot(H[0])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de rojos modificada")
        plt.grid()
        plt.show()
        
        plt.plot(H[1])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de verdes modificada")
        plt.grid()
        plt.show()
        
        plt.plot(H[2])
        plt.xlabel("Valor del píxel")
        plt.ylabel("Frecuencia")
        plt.title("Escala de azules modificada")
        plt.grid()
        plt.show()