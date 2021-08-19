import math

global count

def enum(N):
    result = [None] * (N + (N + 1))
    enum_aux(N, 0, result)

def enum_aux(N, index, result):
    if N == 0:
        if result[1:3] == [1]*2 or result[len(result)-4:len(result)-2] == [0]*2:
            return
        result[index:] = [1] * (len(result) - index)
        print( str(result))
    elif result[0] == 1:
        return
    elif index == len(result)-2:
        return
    else:
        result[index] = 0
        enum_aux(N-1, index + 1, result)
        result[index] = 1
        enum_aux(N, index + 1, result)

def num_FBT(N):
    return int(math.factorial(2*N)//((math.factorial(N+1)*math.factorial(N))))

def main():
    N = 4
    for i in range(N + 1):
        enum(i)
        tree_number = num_FBT(i) + i

main()
