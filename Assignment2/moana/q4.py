def lzss_compress(txt, dic, buff):
    #beginning of the window
    i = 0
    #beginning of the buffer
    j = 0

    while j < len(txt):
        print('\ni: ' + str(i) + '    j: ' + str(j))
        Dic = txt[i:j]
        Buff = txt[j : j + buff]

        print('BUFF: ' + str(Buff))
        print('DIC: ' + str(Dic))

        (offset, length) = longest_match(Dic, Buff)
        print('offset: ' + str(offset) + ' length: ' + str(length))
        if length >= 3:
            offset1 = (0, offset, length)
            print('offset1 : ' + str(offset1))
        else:
            offset2 = (1, txt[j])
            length = 1
            print('offset2: ' + str(offset2))

        j += length
        i = j - dic

        
        if i < 0:
            i = 0


def longest_match(Dic, Buff):
    n_dic = len(Dic)
    n_buff = len(Buff)
    Window = Dic + Buff
    pointer = (0, 0)
    
    for i in range(n_dic):
        j = 0
        if Buff[j] == Dic[i]:
            while Buff[j] == Window[i+j]:
                j += 1
                if j == n_buff:
                    break
            if pointer[1] < j:
                pointer = (n_dic - i, j)
    print(pointer)           
    return pointer

lzss_compress('aacaacabcaba', 6, 4)
