import sys
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
    print('z_box: ' + str(z_box))
    position = 0
    for i in range(m-1):
        position = m - z_box[i]
        if position < m:
            GoodSuffix[position] = i
    return GoodSuffix

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
    print(z_box)

    max_val = 0
    for i in range(m-1, -1, -1):
        if  z_box[i] > max_val:
            max_val = z_box[i]
        MatchedPrefix[i] = max_val
    return MatchedPrefix
        

def boyer_moore(txt, pat):
    '''
-This function computes the hamming distnace between two strings
of equal lengths.
-reads in 2 plain text files
Time Complexity: O(n + m)
'''
    m = len(pat)
    n = len(txt)
    result = [None]*n
    
    #print both txt and pat
    
    LookUp = lookup_table(pat)
    GoodSuffix = preprocess_goodsuffix(pat)
    MatchedPrefix = preprocess_matchedprefix(pat)
    print('good suffix: ' + str(GoodSuffix))
    print('matched prefix: ' + str(MatchedPrefix))
    #print(LookUp)

    i = 0
    shift = 0
    while i <= n-m:
        shift_badchar = 1
        shift_goodsuffix = 1
        mismatched = False
        #find mismatch from left to right
        j = m-1
        while j>=0 or i+j > n:
            if pat[j] != txt[i+j]:
                #Bad Character
                shift_badchar = LookUp[ord(txt[i+j])][j]
                
                if shift_badchar < 0:
                    shift_badchar = j + 1

               #print('shift_badchar: ' + str(shift_badchar))
            
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
                        
                print('bad character shift ' + str(shift_badchar))
                print('good suffix shift ' + str(shift_goodsuffix))
                shift = max(shift_badchar, shift_goodsuffix)
                print('shift: ' + str(shift) + '\n')
                mismatched = True
                break
            #elif j == 0 and count == 0:
                #shift = m
            j-=1
        if not mismatched:
            shift = m
            print(str(i+1))
        i += shift

    return result
        
def main():
    txt = []
    pat = []
    try:
        for line in open(sys.argv[1], 'r'):
            for c in line:
                txt.append(c)
    except FileNotFoundError:
        print("File not found!")

    try:
        for line in open(sys.argv[2], 'r'):
            for c in line:
                pat.append(c)
    except FileNotFoundError:
        print("File not found!")

    HD = search_hammingdist(txt, pat)
    f = open('output_hammingdist.txt', 'w')
    for i in range(len(HD)):
        if HD[i] is not None:
            f.write(str(i) + ' ' + str(HD[i]))
            f.write('\n')
    f.close()
            
if __name__ == "__main__":
    #main() 

    boyer_moore('abcccab', 'aac') 
