from random import randint

def randomString(n, p):
    s = [None]*n
    f = open("randomString.txt", "w+")

    if p <= 1 and p >= 0:
        probH = int(n*p)
        probT = int(n*(1-p))
        count = 0
        
        while count < n and (probH > 0 and probT > 0):

            binaryAlph = randint(0, 1)

            if binaryAlph == 0:
                s[count] = 'H'
                probH -=1
                count += 1
                
            else:
                s[count] = 'T'
                probT -=1
                count += 1

        remaining = n - probH - probT
        if probH < 1:
            for i in range(remaining, n, 1):
                s[i] = 'T'
        if probT < 1:
            for i in range(remaining, n, 1):
                s[i] = 'H'

    for item in s:
        f.write(item)

if __name__ == "__main__":
    randomString(10, 0.3)
