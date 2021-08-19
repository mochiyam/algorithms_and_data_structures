
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
    print(z_box)

    position = 0
    for i in range(m-1):
        position = m - z_box[i]
        if position < m:
            GoodSuffix[position] = i
    print(GoodSuffix)
    return GoodSuffix

def preprocess_matchedprefix(string):
    m = len(string)
    MatchedPrefix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string)
    print(z_box)
    
    max_val = 0
    for i in range(m-1, -1, -1):
        if  z_box[i] > max_val:
            max_val = z_box[i]
        MatchedPrefix[i] = max_val
    print(MatchedPrefix)
    return MatchedPrefix
        

def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)
    
    #print both txt and pat
    print(txt)
    print(pat)

    BadChar = preprocess_badchar(pat)
    GoodSuffix = preprocess_goodsuffix(pat)
    MatchedPrefix = preprocess_matchedprefix(pat)

    i = 0
    j = m - 1

    #find number of shifts for Bad Character
    while i <= n-m:
        shift_badchar = 1
        #find mismatch from left to right
        for j in range(m-1, -1, -1):
            if pat[j] != txt[i+j]:
                char_x = txt[i+j]
                if BadChar[ord(char_x)] != None:
                    #max(1, k-R(x))
                    if j-BadChar[ord(char_x)] > 1:
                        shift_badchar = j - BadChar[ord(char_x)]
                        break;
                    #if the mismatching character is not present: R(x) = 0
                    else:
                        shift_badchar = 1
                        break;
        print('shift ' + str(shift_badchar))
        i += shift_badchar

    print('/n')
    i = 0
    j = m - 1
    #find number of shifts for Good Suffix
    while i <= n-m:
        shift_goodsuffix = 1
        #find mismtch from left to right
        for j in range(m-1, -1, -1):
            if pat[j] != txt[i+j]:
                #case 1a
                if GoodSuffix[j+1] > -1:
                    shift_goodsuffix = m - GoodSuffix[j+1] -1
                    break
                #case 1b
                elif GoodSuffix[j+1] == -1:
                    shift_goodsuffix = m - MatchedPrefix[j+1]
                    break
                #case 2:
                    shift_goodsuffix = m
                    break

        
        i += shift_goodsuffix
        print(i)
                    

if __name__ == "__main__":

    boyer_moore('abaaabcb', 'abcbab')    
