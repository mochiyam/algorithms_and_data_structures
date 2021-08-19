def z_box(new_string):
    # initialize the array
    z_array = [0] * len(new_string)
    z_array[0] = len(new_string)
    # initialize the box boundary
    left = 0
    right = 0
    # loop through the string, skipping 0
    for i in range(1, len(new_string)):
        # if outside the z-box, then we need to count
        if i > right:
            count = 0
            # while we are still within the string
            # and the letter is the same as the prefix
            # note: count keep track of the prefix
            while i + count < len(new_string) and new_string[count] == new_string[i+count]:
                # increment count
                count += 1
            # set the z-value at i
            z_array[i] = count
            # if there is a box, update the box boundary
            if count > 0:
                left = i
                right = i + count - 1
        # if it is within the box
        # i <= right
        else:
            # get the paired prefix index (z-value) to copy
            index_prefix = i - left
            # the remaining length of the box
            remaining = right - i + 1
            # case 2a
            # if the z-value at prefix is still within the remaining box
            if z_array[index_prefix] < remaining:
                # copy the value
                z_array[i] = z_array[index_prefix]
            # case 2b
            # if the value is the exactly the box
            # then we need to extend/ find a new box
            elif z_array[index_prefix] == remaining:
                new_right = right + 1
                while new_right < len(new_string) and new_string[new_right] == new_string[new_right-i]:
                    new_right += 1
                # update the z-array with the extension
                z_array[i] = new_right - i
                # new left and right boundary
                left = i
                right = new_right - 1
            # case 2c
            # if the value is greater than the remaining (going outside the box)
            # then we know only the remaining of the box is the same as the prefix
            # note this is z_array[index_prefix] > remaining
            else:
                z_array[i] = remaining
    # return the z-array
    return z_array

def run():
    # the input
    my_string = "cddacddac"
    # testing the z-algorithm
    z_array = z_box(my_string)
    print(my_string)
    print(z_array)

if __name__ == "__main__":
    run()
