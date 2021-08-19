import random
import math

def naive_prime_test(n):
    for k in range(2, n, 1):
        print(k)
        if n % k == 0:
            return "composite!"
    return "prime!"

def fermat_randomized_test(n):
    a = random.randint(1, n+1)
    if(a**(n-1) % n != 1):
        return "composite!"
    return "maybe prime!"

def isEven(x):
    return x % 2 == 0

def isPrime(n, k):
    '''
miller rabin
'''
    if n == 2:
        return True
    if isEven(n):
        return False
    s = 0
    t = n-1
    while isEven(n):
        s += 1
        t /= 2

    for _ in range(k):
        a = random.randint(2, n-1)
        if (a**(n-1) % n != 1):
            return False
        for i in range(1, s+1, 1):
            if (a**((2**i)*t) % n == 1) and ((a**(2**(i-1)*t) % n != 1) or (a**(2**(i-1)*t) % n != -1)):
                return False
    return True
            
# print(miller_rabin(521, 10))


def factors(N):
    C = [[0 for x in range(2)] for y in range(101)]
    P = [0] * 100
    N_Array = [0] * N
#    result = [[0 for x in range(2)] for y in range(101)]

    i = 0
    while i < 100:
        if N == 1:
            break
        if isPrime(N, 10):
            P[i] = N
            N_Array[N] = 1
            i += 1
        N -= 1
        
    for i in range(len(P)):
        C[i][0] = P[i] + 1

    print(P)
    print(C)
    print(N_Array)

    for i in range(len(C)):
        while  C[i][0] % 2 == 0:
            C[i][1] += 2
            C[i][0] /= 2

        for i in range(3, int(math.sqrt(C[i][0])) + 1, 2):
            while C[i][0]% i == 0:
                C[i][1] = i
                C[i][0] /= i
        if C[i][0] > 2:
            C[i][1] += C[i][0]



factors(545)
#print(isPrime(545, 10))


        
