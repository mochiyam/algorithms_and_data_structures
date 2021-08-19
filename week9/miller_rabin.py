import random

def millerRabinRandomizedPrimality(n, k):
    isComposite = True
    if n%2 == 0:
        return isComposite
    
    s = 0
    t = n - 1
    while(t%2 == 0):
        s += 1
        t /= 2

    for _ in range(k): 
        a = random.randint(2, n-1)
        if (a**(n-1) % n) != 1:
            return isComposite
        for i in range(1, s+1):
            if ((a**(2**i.t) % n == 1) and (a**(2**(i-1).t)% n != 1 or (a**(2**(i-1).t)% n != -1))):
                return isComposite
    return not isComposite  
            
        
    
