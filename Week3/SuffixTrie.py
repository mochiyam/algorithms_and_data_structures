class Node:
    def __init__(self):
        ascii_char = 256
        self.children = [None]*ascii_char
        self.mark_as_end = False
      
class SuffixTree:
    def __init__(self):
        self.root = self._getNode()

    def _getNode(self):
        return Node()

    def _index(self, c):
        return ord(c)

    def _construct(self, key):
        self.root = self._construct_aux(self.root, key)
        
    def _construct_aux(self, current, key):
        for c in key:
            index = self._index(c)
            if not current.children[index]:
                current.children[index]
                current.children[index] = self._getNode()
            current = current.children[index]
        current.mark_as_end = True

def main():
    st = SuffixTree()
    string = 'BANANA'

    st._construct(string)

    for item in st:
        print(item, end = ", ")
    
if __name__ == '__main__':
    main()
