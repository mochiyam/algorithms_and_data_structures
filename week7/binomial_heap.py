import math

class Node:
    def __init__(self, key = None):
        self.key = key
        self.payload  = None
        self.degree = None
        
        self.parent = None
        self.left_child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def get_root(self):
        self.swap

    def swap(self, a, b):
        self.a

    def insert(self, x):
        new_heap = BinomialHeap()
        new_heap.head = Node(x)
        count += 1

    def merge(self, old_heap, new_heap):
        old_heap.head = new_heap
    
    def min(self):
        current = self.head
        min_value = math.inf
        min_node = None
        while current is not None:
            if current.key < min_value:
                min_value = current.key
                min_node = current
            current = current.sibling
        return min_node

    def extract_min(self):
        min_node = self.min()
        delete(min_node)

        make_heap = BinomialHeap()
        make_heap.head = current.
        
        
            
        
        
            
            
            
    
#def delete(self, x):
#http://www.cs.toronto.edu/~anikolov/CSC265F16/binomial-heaps.pdf
        

        



