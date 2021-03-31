

def Bordesx(i,a,b,t):
    if t==0: #Réplica
        if i<0:
            i=0
        elif i>a-1:
            i=a-1
            
    if t==1: #Simétrico
        if i<0:
            i=abs(i)+i
        
        elif i>a:
            i=i-b
        
        
    if t==2: #Periódico
        if i<1:
            i=a+i
        elif i>a:
            i=i-a
    
    return i