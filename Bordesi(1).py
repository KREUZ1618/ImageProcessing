# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:21:01 2020

@author: DELL
"""
import numpy as np
def Bordesi(i,M,m,t):
    if t==0: #Réplica
        if i<0:
            i=0
        elif i>M-1:
            i=M-1
            
    if t==1: #Simétrica
        if i<0:
            i=abs(i)+i
        
        elif i>M:
            i=i-m
        
        
    if t==2: #Periódica
        if i<1:
            i=M+i
        elif i>M:
            i=i-M
    
    return i