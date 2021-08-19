class Vertex:
    '''
Initializes once an object Vertex of a class is instantiated
'''
    def __init__(self, item = None, link = None):
        self.item = item
        self.next = link

class AdjList:
    '''
Initializes once an object AdjList of a class is instantiated
'''
    def __init__(self):
        self.head = None
        self.count = 0
    
    def insert(self, item):
        '''
    This function inserts vertex into the auxilary function
    :param: item: vertex item to be added in the list
    Time Complexity: O(1)
'''
        current = self.head
        if current is None:
            self.head = Vertex(item, self.head)
        else:
            while(current.next is not None):
                current = current.next
            current.next = Vertex(item)
        self.count += 1

    def contains(self, vertex):
        return self.contains_aux(self.head, vertex)
    
    def contains_aux(self, current, vertex):
        if current is None:
            return False
        return current.item == vertex or self.contains_aux(current.next, vertex)

    def __len__(self):
        return self.count

