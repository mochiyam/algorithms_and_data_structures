def zAlgorithm(s):
    right = 0
    left = 0
    n = len(s)
    z_box = [0]*len(s)
    z_box[0] = len(s)

    for k in range(1, n):
        #when k is not in the current z-box
        if k > right:
            count = 0
            while count + k < n and s[count] == s[count + k]:
                count += 1
            z_box[k] = count
            if z_box[k] > 0:
                right = count+k-1
                left = k
        #if k <= right : when k is inside the current z-box
        else:
            remaining = right-k+1
            pair_index = k - left
            if z_box[pair_index] < remaining:
                z_box[k] = z_box[pair_index]
            elif z_box[pair_index] > remaining:
                z_box[k] = remaining
            # z_box[pair_index] = remaining
            else:
                q = right+1
                print(q)
                while right < n and s[q] == s[q-k]:
                    print(q)
                    q+=1
                z_box[k] = q-k
                right = q-1
                left = k
    return z_box
        
def find_occurences(txt, pat):
    '''
    pat[1..m] + $ + txt[1..n]
    '''
    occurence = []
    m = len(pat)
    n = len(txt)
    s = pat + '$' + txt
    z_box = zAlgorithm(s)

    for i in range(m+1, n+m, 1):
        if z_box[i] == m:
            occurence.append(i - m -1)            
    return occurence

def naiveAlgorithm(txt, pat):
    m = len(pat)
    n = len(txt)
    occurence = []

    for i in range(n-m+1):
        count = 0
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
            else:
                count += 1
        if j == m-1:
            occurence.append(i)
    return occurence
    
if __name__ == "__main__":

    txt = input("Give a reference text: ")
    pat = input("Give a pattern: ")

    z_occurence = find_occurences(txt, pat)
    naive_occurence = naiveAlgorithm(txt, pat)

    print(z_occurence)
    print(naive_occurence)




    
