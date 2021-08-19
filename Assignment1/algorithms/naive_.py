from z_algorithm import z_algorithm

def preprocess_badchar(string):
    ascii_char = 256
    BadChar = [None]* ascii_char
    m = len(string)

    for i in range(m-1, -1, -1):
        if BadChar[ord(string[i])]== None:
            BadChar[ord(string[i])] = i
    return BadChar

def preprocess_goodsuffix(string):
    m = len(string)
    GoodSuffix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string[::-1])[::-1]

    position = 0
    for i in range(m-1):
        position = m - z_box[i]
        if position < m:
            GoodSuffix[position] = i
    return GoodSuffix

def preprocess_matchedprefix(string):
    m = len(string)
    MatchedPrefix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string)
    
    max_val = 0
    for i in range(m-1, -1, -1):
        if  z_box[i] > max_val:
            max_val = z_box[i]
        MatchedPrefix[i] = max_val
    return MatchedPrefix

def find_badchar_shift(BadChar, j, char_x):
    shift_badchar = 1
    if BadChar[ord(char_x)] != None:
    #max(1, k-R(x))
        if j-BadChar[ord(char_x)] > 1:
            shift_badchar = j - BadChar[ord(char_x)]
        #if the mismatching character is not present: R(x) = 0
        else:
            shift_badchar = 1
        
    return shift_badchar

def find_goodsuffix_shift(GoodSuffix, MatchedPrefix, m, txt, i, j):
    shift_goodsuffix = 1
    print('GoodSuffix ' + str(GoodSuffix) + ' ' + str(j))
    print('MatchedPrefix ' + str(MatchedPrefix))

    if j == m-1:
        shift_goodsuffix = 1
    else:
        #case 1a
        if GoodSuffix[j+1] > -1:
            shift_goodsuffix = m - GoodSuffix[j+1] -1
        #case 1b
        elif GoodSuffix[j+1] == -1:
            if MatchedPrefix[j+1] == 0:
                shift_goodsuffix = 1
            else:
                shift_goodsuffix = m - MatchedPrefix[j+1]
        elif j==0:
            shift_goodsuffix = m
        print('shift_goodsuffix' + str(shift_goodsuffix))
        p = GoodSuffix[j+1]
        print('position ' + str(i+p) + ' i+j+2 ' + str(i+j+2) + ' i+m ' + str(i+m) + ' i+m+(j+1-p)+1 ' + str(i+ m+(j+1-p)+1))
        print(txt[i+p:i+j+2])
        print(txt[i+m:i+m+(j+1-p)+1])
        if txt[i+p:i+j+2]== txt[i+m:i+m+(j+1-p)+1]:
            print('hi')
            shift_goodsuffix = 1

    return shift_goodsuffix

def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)

    BadChar = preprocess_badchar(pat)
    GoodSuffix = preprocess_goodsuffix(pat)
    MatchedPrefix = preprocess_matchedprefix(pat)

    i = 0
    shift = 0

    #find number of shifts for Bad Character
    while i <= n-m:
        j = m - 1
        shift_count = 0
        #find mismatch from left to right
        while j>=0:
            #print('i= ' + str(i) + ' j= ' + str(j))
            if shift_count > 1:
                #print('MORE THAN 1 SHIFT')
                break
                
            if pat[j] != txt[i+j]:
                shift = max(find_badchar_shift(BadChar, j, txt[i+j]),find_goodsuffix_shift(GoodSuffix, MatchedPrefix, m, txt ,i,  j))
                #condition                
                shift_count += 1
                print ('shift here ' + str(shift) + str(i) + str(j))
                #print('over here')
            j -=1
        if shift_count <= 1:
            #print('hi')
            print(str(i+1) + '  ' + str(shift_count))
        print('///shift this much ' + str(shift) + '///\n')
        i += shift

                    

if __name__ == "__main__":

     boyer_moore('abxabcabxabxabx', 'abxabxa')

    
