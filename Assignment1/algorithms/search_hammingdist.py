from z_algorithm import z_algorithm

def lookup_table(string):
    '''
-This function preprocesses good suffix using string 'pat'
-Implemented extension to bad character shift rule by
creating a look up table to store number of shifts
-Will be used for good suffix shift
Space Complexity: O(m*N) where N is number of ascii character = 256
'''
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
    '''
-This function preprocesses good suffix using string 'pat'
-Will be used for good suffix shift
'''
    ascii_char = 256
    BadChar = [None]* ascii_char
    m = len(string)

    for i in range(m-1, -1, -1):
        if BadChar[ord(string[i])]== None:
            BadChar[ord(string[i])] = i
    return BadChar

def preprocess_goodsuffix(string):
    '''
-This function preprocesses good suffix using string 'pat'
-Will be used for good suffix shift
Auxilary Space: O(m)
Time Compelxity: O(m)
'''
    m = len(string)
    GoodSuffix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string[::-1])[::-1]
    #print('reverse zbox: ' + str(z_box))
    position = 0
    for i in range(m-1):
        position = m - z_box[i]
        if position < m:
            GoodSuffix[position] = i

    #calculate the total number of Good Suffix
    total_GS = 0
    for x in GoodSuffix:
        total_GS += x
        
    #print ('good suffix: ' + str(GoodSuffix))
    return GoodSuffix, total_GS

def preprocess_matchedprefix(string):
    '''
-This function preprocesses matched prefix using string 'pat'
-Will be used for good suffix shift
Auxilary Space: O(m)
Time Compelxity: O(m)
'''
    m = len(string)
    MatchedPrefix = [-1]*m

    #compute z-Algorithm
    z_box = z_algorithm(string)
    #print('zbox: ' + str(z_box))
    
    max_val = 0
    for i in range(m-1, -1, -1):
        if  z_box[i] > max_val:
            max_val = z_box[i]
        MatchedPrefix[i] = max_val
    #print('matchd prefix: '  + str(MatchedPrefix))
    return MatchedPrefix
        

def search_hammingdist(txt, pat):
    '''
-This function computes the hamming distnace between two strings
of equal lengths.
-reads in 2 plain text files
Time Complexity: O(n + m)
'''
    m = len(pat)
    n = len(txt)
    result = [0] + [-1] * n
    
    LookUp = lookup_table(pat)
    GoodSuffix, total_GS = preprocess_goodsuffix(pat)
    MatchedPrefix = preprocess_matchedprefix(pat)

    i = 0
    shift = 0
    #total number of hamming distance >= 1 in a string
    total = 0
    while i <= n-m:
        shift_badchar = 1
        shift_goodsuffix = 1
        count = 0
        #find mismatch from left to right
        j = m-1
        while j>=0 or i+j > n:
            #print('i: ' + str(i) + '    j: ' + str(j))
            if j == 0 and pat[j] == txt[i+j] and count == 0:
                shift = m
                break
            if pat[j] != txt[i+j]:
                #if count > 1:
                    #break;
                #Bad Character
                shift_badchar = LookUp[ord(txt[i+j])][j]
                if shift_badchar < 0:
                    shift_badchar = 1

                if total_GS == -1*m:
                    shift_goodsuffix = -1
                
                #Good Suffix
                elif j == m-1:
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
            total += 1
            result[i+1] = count
        i += shift
    #0th position stores total number of hamming distance of a string
    result[0] = total
    print(result)
    return result
        #print('j: ' + str(i))
        #print('bad character shift ' + str(shift_badchar))
        #print('good suffix shift ' + str(shift_goodsuffix))

        #print('shift ' + str(shift))
        
                    

if __name__ == "__main__":

    search_hammingdist('dy', 'cy')    
