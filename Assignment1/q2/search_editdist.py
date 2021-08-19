from search_hammingdist import search_hammingdist

def search_editdist(txt, pat):
    '''
-This function computes the edit distance between two strings
through a text file and 
-reads in 2 plain text files
Time Complexity:
'''
    n = len(txt)
    m = len(pat)
    #length of the largest substring
    #no matter where mismatch occurs
    half_len = m//2

    i = 0
    shift = 0
    while i <= n -m:
        #count edit distance
        j = 0
        while j < m or i+j > n:
            if pat[0:m] == txt[i: i+m]:
                print(str(i+1) + '  0') 
                shift = m 
                break
            #if a mismatch occurs:
            elif pat[j] != txt[i+j]:
                #check the hamming distance of new_txt and new_pat
                new_txt = txt[i+j : i + m]
                new_pat = pat[j : m]
                print(new_txt)
                print(new_pat)

                result = search_hammingdist(new_txt, new_pat)
                #Substitution
                #since only 1 hamming distance
                if result[0] == 1:
                    print('substituion!')
                    print(str(i+1) + '  1') 
                    shift = m
                    break

                #Deletion
                if txt[i+j : i + m - 1] == pat[j+1 : m]:
                    print('deletion!')
                    print(txt[i+j : i + m - 1])
                    print(pat[j+1 : m])
                    print(str(i+1) + '  1') 
                    shift = m - 1
                    break

            shift+=1
            j+=1
        i+=shift

    def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)
    print(txt)
    print(pat)
    
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
        #find mismatch from left to right
        j = m-1
        while j>=0 or i+j > n:
            if j == 0 and pat[j] == txt[i+j]:
                shift = m
                break
            if pat[j] != txt[i+j]:

                #Bad Character
                shift_badchar = LookUp[ord(txt[i+j])][j]
                if shift_badchar < 0:
                    shift_badchar = 1

                if j == m-1:
                        shift_goodsuffix = 1
                else:
                #Good Suffix
                    #case 1a
                    if GoodSuffix[j+1] > -1:
                        shift_goodsuffix = m - GoodSuffix[j+1] -1
                    #case 1b
                    elif GoodSuffix[j+1] == -1:
                        shift_goodsuffix = m - MatchedPrefix[j+1]

                    #case 2:
                    elif j==0:
                        shift_goodsuffix = m
                    
                shift = max(shift_badchar, shift_goodsuffix)
                break
            j-=1
        i += shift
        print(i)
        print('bad character shift ' + str(shift_badchar))
        print('good suffix shift ' + str(shift_goodsuffix))
        print('shift ' + str(shift))

def main():
    txt = []
    pat = []
    try:
        for line in open((sys.argv[1], 'r')):
            for c in line:
                txt.append(c)
    except FileNotFoundError:
        print("File not found!")

        for line in open((sys.argv[2], 'r')):
            for c in line:
                pat.append(c)
    except FileNotFoundError:
        print("File not found!")
        
    EditDistance = search_editdist(txt, pat)
    f = open('output_kruscal.txt', 'w')
    '''current = MST.head
    while current is not None:
        for i in range(3):
            f.write(str(current.item[i]) + ' ')
        f.write("\n")
        current = current.next
    f.close()
    '''
if __name__ == "__main__":
    #main()
    search_editdist('abdyabxdcyabcdz', 'abcd')
