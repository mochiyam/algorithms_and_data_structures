def z_algorithm(string):
    '''
-This function calculates the Gusfield's z-algorithm using a string value
Time Complexity: O(n)
'''
    n = len(string)
    z_box = [0]*len(string)
    z_box[0] = len(string)
    
    #initizalize the pointer
    right = 0
    left = 0

    for k in range(1, n):
        #when k is not in the current z-box
        if k > right:
            count = 0
            while count + k < n and string[count] == string[count + k]:
                count += 1
            z_box[k] = count
            if z_box[k] > 0:
                right = count+k-1
                left = k
        #if k <= right : when k is inside the current z-box
        else:
            #remaining length of the box
            remaining = right-k+1
            pair_index = k - left
            #case 2a
            if z_box[pair_index] < remaining:
                z_box[k] = z_box[pair_index]
            # case 2b
            elif  z_box[pair_index] == remaining:
                q = right+1
                while q < n and string[q] == string[q-k]:
                    q+=1
                z_box[k] = q-k
                left = k
                right = k + q-1
            #case 2c (subset of case 2b): z_box[pair_index] > remaining
            else:
                z_box[k] = remaining
    return z_box

