
def Bordesy(j,a,b,t):

    if t==0: #Réplica
        if j<0:
            j=0
            
        elif j>a-1:
            j=a-1
    
    
    if t==1: #Simétrico
        if j<1:
            j=abs(j)+j
        
        elif j>a:
            j=j-b
    
    
    if t==2: #Periódico
        if j<0:
            j=j+a
        if j>a:
            j=j-a
    
    return j