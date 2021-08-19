def elias_code():
    value = 'abcdef'
    unicode = []
    bin_string = []
    
    for i in value:
        unicode.append(ord(i))

    for i in unicode:
        bin_string.append(bin(i)[2:])

    print(unicode)
    print(bin_string)

    N = len(bin_string[0])

    len_component = N
    for i in range(N, -1, -1):
        len_component =- 1
        
    

elias_code()
