import random
from collections import Counter
def counter_version(n,a,b):
    
    count=Counter()
    
    for _ in range(n):
        x=random.randint(a,b)
        for i in range (a,x+1):
            count[i]+=1
    
    for i in range(a,b+1):
        if count[i]<=n/2:
            return i
    
    return None


counter_version(10000,50,55)