
from z_algorithm import z_algorithm

def lookup_table(string):
    ascii_char = 256
    m = len(string)

    LookUp = [[-1 for i in range(m)] for j in range(ascii_char)]

    for i in range(m):
        c = string[i]
        LookUp[ord(c)][i] = 0

    for i in range(ascii_char):
        index = -1
        for j in range(m):
            if LookUp[i][j] == 0:
                index = j
            elif index > -1:
                LookUp[i][j] = j- index
                
    return LookUp

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
    print('reverse zbox: ' + str(z_box))
    position = 0
    for i in range(m-1):
        position = m - z_box[i]
        if position < m:
            GoodSuffix[position] = i
    print(m)
    print ('good suffix: ' + str(GoodSuffix))
    return GoodSuffix

def preprocess_matchedprefix(string):
    m = len(string)
    MatchedPrefix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string)
    print('zbox: ' + str(z_box))
    
    max_val = 0
    for i in range(m-1, -1, -1):
        if  z_box[i] > max_val:
            max_val = z_box[i]
        MatchedPrefix[i] = max_val
    print('matchd prefix: '  + str(MatchedPrefix))
    return MatchedPrefix
        

def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)
    
    #print both txt and pat
    
    LookUp = lookup_table(pat)
    #BadChar = preprocess_badchar(pat)
    GoodSuffix = preprocess_goodsuffix(pat)
    MatchedPrefix = preprocess_matchedprefix(pat)

    i = 0
    shift = 0
    while i <= n-m:
        shift_badchar = 1
        shift_goodsuffix = 1
        count = 0
        #find mismatch from left to right
        j = m-1
        while j>=0 or i+j > n:
            #print('i: ' + str(i) + '    j: ' + str(j))
            if j == 0 and pat[j] == txt[i+j]:
                shift = m
                break
            if pat[j] != txt[i+j]:
                if count > 1:
                    break;
                #Bad Character
                shift_badchar = LookUp[ord(txt[i+j])][j]
                if shift_badchar < 0:
                    shift_badchar = 1
            
                #Good Suffix
                if j == m-1:
                    shift_goodsuffix = 1
                 #case 1a
                else:
                    if GoodSuffix[j+1] > -1:
                        shift_goodsuffix = m - GoodSuffix[j+1] -1
                    #case 1b
                    elif GoodSuffix[j+1] == -1:
                        shift_goodsuffix = m - MatchedPrefix[j+1]

                    #case 2:
                    elif j==0:
                        shift_goodsuffix = m
                        
                shift = max(shift_badchar, shift_goodsuffix)
                count += 1
            j-=1
        if count <=1:
            print(str(i+1) + '    ' + str(count))
        i += shift
        #print('j: ' + str(i))
        #print('bad character shift ' + str(shift_badchar))
        #print('good suffix shift ' + str(shift_goodsuffix))
        #print('shift ' + str(shift))

                    

if __name__ == "__main__":

    boyer_moore('bbcaefadcabcpqr', 'abc')    
