from Quicksort import quicksort
class Node:
    
    def __init__(self, char, freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    

class HuffmanCode:
    '''
Assign bit symbol 0 to the left branch
Assign bit symbol 1 to the right branch 
'''
    def __init__(self, text):
        self.text = text

    def make_freq(self):
        freq = [0] * 256
        ascii_char = ''
        
        for ch in self.text:
            freq[ord(i)] +=1
        return freq

    def make_binary_tree():
        n = len(freq)
        freq = make_freq()
        order = quicksort(freq, 0, n)
        
        

    
def main():
