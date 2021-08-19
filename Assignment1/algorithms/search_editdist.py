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
        count = 0
        j = m - 1
        while j>=0 or i+j > n:
            if pat[0:m] == txt[i: i+m]:
                shift = m
                break
            #if a mismatch occurs:
            elif pat[j] != txt[i+j]:
                #check if position j is < half of the length m
                if j >= half_len:
                    #only one mismatch has occured
                    if pat[0:half_len] == txt[i:i + half_len]:
                        #check the hamming distance of new_txt and new_pat
                        new_txt = txt[i+ half_len : i + m]
                        new_pat = pat[half_len : m]

                        result = search_hammingdist(new_txt, new_pat)
                        #result[0] stores number of hamming distance >= 0
                        if result[0] != 0:
                            #edit distance: substitution or insertion
                            shift = m
                            count += 1
                            break
                        else:
                            #edit distance: deletion
                            #create new txt two times the length of substring txt
                            del_new_txt = txt[i+ half_len : i + m] + txt[i+ half_len : i + m]
                            del_result = search_hammingdist(del_new_txt, new_pat)
                            
                            if del_result[0] != 0:
                                 shift = m - 1
                                 count += 1
                                 break
                                
                            #edit distance: insertion
                            ins_new_txt = txt[i + half_len : i + m + 1]
                            ins_result = search_hammingdist(ins_new_txt, new_pat)

                            if ins_result[0] != 0:
                                 shift = m + 1
                                 count += 1
                                 break
                                 
                    #if pat[0:half_len] != txt[i:i + half_len]    
                    else:
                        shift = 1
                        count = -1
                        break
            j-=1
        if count != -1:
            print(str(i+1) + '  ' + str(count))
        i += shift

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

