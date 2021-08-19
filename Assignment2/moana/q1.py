import math
import random

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

def factors(N):
    C = [0] * 100
    P = [0] * (N + 1)
    Table = [[0 for x in range(N)] for y in range(100)]


    num = N
    for _ in range(N):
        if num == 1:
            break
        if isPrime(num, 10):
            P[num] = 1
        num -= 1

    i = len(C) - 1
    j = len(P) - 1
    while i > -1:
        if P[j] == 1:
            C[i] = j + 1
            i -= 1
        j -= 1

    #print(C)

    result  = [[] for y in range(100)]
    i = 0

    while i < len(C):
        x = int(C[i])
        while P[int(x)] != 1:
            if C[i] % 2 == 0:
                result[i].append(2)
                x /= 2
            elif C[i] % 3 == 0:
                result[i].append(3)
                x /= 3
            else:
                break
        if x == 1:
            break
        else:
            if P[int(x)] == 1:
                result[i].append(int(x))
        result[i].append(None)
        i+=1

    #print(result)

    for i in range(len(result)):
        j = 0
        print(str(C[i]) + '    ' + str(result[i][j]) + '^', end='')
        j+=1
        count = 1
        while result[i][j] != None:
            if result[i][j] == result[i][j-1]:
                count += 1
            else:
                count = 1
                print(str(count) + ' x ' + str(result[i][j]) + '^', end='')
            j += 1
        print(str(count))
    
factors(542)
