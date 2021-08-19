def binary_mode(aList):
    #number of unique ASCII characters
    n_unique = 0
    #total number of characters in input file
    n_char = len(aList)
    #frequency of each distinct character
    freq = [0] * 256

    binary_mode = ''

    for i in aList:
        ascii_char = ord(i)
        freq[ascii_char] += 1
        if freq[ascii_char] == 1:
            n_unique += 1

    binary_mode += elias_code(n_unique)
    binary_mode += elias_code(freq)
    binary_mode += elias_code(n_char)
    
            
def elias_code(value):
    #minimal binary code
    encode = []
    value = bin(value)[2:]
    len_component = len(value) - 1
    min_bin_code = ""

    encode.append(value)
    while len_component != 0:
        min_bin_code = '0' + bin(len_component)[3:]
        len_component = len(min_bin_code) - 1
        encode.append(min_bin_code)
        print(min_bin_code)

    print(encode[::-1])

    encode_string = ""
    for i in encode[::-1]:
        encode_string += i
    print(encode_string)
    return encode_string

def huffman_code():
    
    
def main():
    aList = []
        
    try:
        filename = open('mywords.txt', 'r')
        for word in filename:
            line = word.strip("\n")
            for ch in line:
                aList.append(ch)
    except FileNotFoundError:
        print("File not found!")
	
    binary_mode(aList)
if __name__ == '__main__':
    #main()
    elias_code(561)
