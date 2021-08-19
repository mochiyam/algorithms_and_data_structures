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
    print('z_box' + str(z_box))

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
    print('Bad Character ' + str(BadChar))
    if BadChar[ord(char_x)] != None:
    #max(1, k-R(x))
        if j-BadChar[ord(char_x)] > 1:
            shift_badchar = j - BadChar[ord(char_x)]
        #if the mismatching character is not present: R(x) = 0
        else:
            shift_badchar = 1
        
    return shift_badchar

def find_goodsuffix_shift(GoodSuffix, MatchedPrefix, m, j):
    shift_goodsuffix = 1
    print('GoodSuffix ' + str(GoodSuffix))
    print('MatchedPrefix ' + str(MatchedPrefix))

    if j == m-1:
        shift_goodsuffix = 1
    #case 1a
    elif GoodSuffix[j+1] > -1:
        shift_goodsuffix = m - GoodSuffix[j+1] -1
    #case 1b
    elif GoodSuffix[j+1] == -1:
        if MatchedPrefix[j+1] == 0:
            shift_goodsuffix = 1
        else:
            shift_goodsuffix = m - MatchedPrefix[j+1]
    #case 2:
    else:
        shift_goodsuffix = m
        
    return shift_goodsuffix

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
    shift = 0

    #find number of shifts for Bad Character
    while i <= n-m:
        j = m - 1
        #find mismatch from left to right
        while j>=0:
            print('i= ' + str(i) + ' j= ' + str(j))
            if pat[j] != txt[i+j]:
                shift = max(find_badchar_shift(BadChar, j, txt[i+j]), find_goodsuffix_shift(GoodSuffix, MatchedPrefix, m , j))
                break                
            elif j == 0:
                shift = m
                break
            else:
                j -=1
        print('///shift this much ' + str(shift) + '///\n')
        i += shift

                    

if __name__ == "__main__":

    boyer_moore('abcbababcbabbcbababcba', 'cab')
    #preprocess_goodsuffix('cddacddac')

    
