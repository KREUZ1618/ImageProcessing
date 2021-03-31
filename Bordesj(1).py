# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:20:25 2020

@author: DELL
"""
import numpy as np
def Bordesj(j,N,n,t):
    index=0
    if t==0: #Réplica
        if j<0:
            j=0
            
        elif j>N-1:
            j=N-1
    
    
    if t==1: #Simétrica
        if j<1:
            j=abs(j)+j
        
        elif j>N:
            j=j-n
    
    
    if t==2: #Periódica
        if j<0:
            j=j+N
        if j>N:
            j=j-N
    
    return j