import random
def list_version(n,a,b):
    
    count=[0]*(b-a+1)
    
    
    for _ in range(n):
        x= random.randint(a, b)
        for i in range(a,x+1):
            count[i-a] +=1
    
    
    for i in range(a,b+1):
        if count[i-a]<= n/2:
            return i
        
    return None
    
    

list_version(10000,50,55)