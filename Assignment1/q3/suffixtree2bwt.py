import sys

#global variable
NUM_CHAR = 256
global_end = -1

class Node:
    '''
-Leaf: self.id > 0
-Root: self.id = -1
-Internal nodes: self.id is None
'''
    def __init__(self, id = None, parent = None):
        self.id = id
        self.edge = [None]*NUM_CHAR
        self.child = [None]*NUM_CHAR
        self.parent = parent
        self.suffix_link = None
        
    def isLeaf(self):
        return self.id is not None and self.id != -1
    
    def getChild(self, x):
        if self.child[x] is not None:
            return self.child[x]
        else:
            return None

    def getDepth(self, x):
        if self.child[x].isLeaf():
            return self.edge[x].getDepth(global_end)
        else:
            return self.edge[x].getDepth(None)

class Edge:
    '''
The edge class stores all the edges in the suffix tree
Implemented trick 2: space efficient representation of edge-label
by representing 2 numbers (start, end) - index
Entire Ukkonen algorithm space complexity: O(n) space
'''
    def __init__(self, start = None, end = None):
        #Trick 2: Space-efficient representation
        self.start = start
        self.end = end

    def setEdge(self, start, end):
        self.start = start
        self.end = end

    def getDepth(self, end):
        if end is None:
            return self.end - self.start + 1
        else:
            return end - self.start + 1

class SuffixTree:
    def __init__(self, string):
        self.root = Node(-1)
        self.string = string
        self.new_internal_node = None
        self.active_node = self.root
        self.active_length = 0
        self.active_edge = -1
        self.remaining = 0

    def activePoint(self):
        return self.active_node.edge[self.active_edge].start + self.active_length

    def splitEdge(self, internal_node, current, new_leaf, char_index, index, position, i):
        #set new parent for the current child
        child = current.getChild(self.active_edge)
        child.parent = internal_node

        #internal node have 2 children
        internal_node.child[ord(self.string[position])] = child
        internal_node.edge[ord(self.string[position])] = Edge(position, global_end)

        internal_node.child[index] = new_leaf
        internal_node.edge[index] = Edge(i, global_end)

        internal_node.suffix_link = self.root
        #parent points to internal node (new child)
        current.child[self.active_edge] = internal_node
        current.edge[self.active_edge].setEdge(current.edge[self.active_edge].start, position-1)

    def traverse(self):
        '''
This (and traverse_aux) is a tail recursive function to manipulate the
trick 1: skip/count trick to skip rapidly through along a path from a
node of a substring.

'''
        length = self.active_node.getDepth(self.active_edge)
        return self.traverse_aux(self.active_node, length)
            
    def traverse_aux(self, current, length):
        if length >= self.active_length:
            return self.activePoint()          
        elif length < self.active_length:
            self.active_node = self.active_node.child[self.active_edge]
            length += self.active_length
            self.active_edge = ord(self.string[length])
            self.traverse_aux(self.active_node, length)                
  
    def construct(self):
        '''
This function constructs an implicit suffix tree using Ukkonen's algorithm
with the string initialized when creating Suffix Link class.
Time Complexity: O(n)
The while(self.remaining)

'''
        n  = len(self.string)

        for i in range(n):
            #Trick 4: fast leaf extension trick
            #increment  global_end 
            global global_end
            global_end = i
            index = ord(self.string[i])
            self.remaining += 1
            self.new_internal_node = None

            while(self.remaining > 0):
                current = self.active_node
                #There are no active edge coming from the active node
                if self.active_length == 0:                  
                    #Rule 2: create a new leaf
                    if current.child[index] is None:
                        current.child[index] = Node(i - self.remaining + 1, current)
                        current.edge[index] = Edge(i, global_end)
                        self.remaining -= 1
                        if current.id != -1:
                            self.active_node = current.suffix_link
                    #Rule 3: No further action
                    else:
                        self.active_edge = index
                        self.active_length += 1
                        if current.getDepth(self.active_edge) == self.active_length:
                            self.active_node = current.child[self.active_edge]
                            self.active_edge = -1
                            self.active_length = 0
                        #Trick 3: premature extension stopping criterion
                        break
                    
                #character is located somehwere in the middle
                #find the character!
                if self.active_length != 0:
                    #Trick 1: skip/count
                    #returns the location of the node and total length of the
                    #substring denoted by the path
                    position = self.traverse()
                    
                    #character located somewhere in the edge of current active_node
                    char_index = ord(self.string[position])
                    #Rule 3: Do nothing
                    if char_index == index:
                        self.active_length += 1

                        if current.getDepth(self.active_edge) == self.active_length:
                            self.active_node = current.child[self.active_edge]
                            self.active_edge = -1
                            self.active_length = 0
                        #Trick 3: premature extension stopping criterion
                        break
                    #if char_index != index
                    else:
                        internal_node = Node(None, current)
                        new_leaf = Node(i - self.remaining + 1, internal_node)
                        self.splitEdge(internal_node, current, new_leaf, char_index, index, position, i)
                        self.remaining -= 1
                        if self.new_internal_node is not None:
                            self.new_internal_node.suffix_link = internal_node
                        self.new_internal_node = internal_node
                        #if active node is at the root
                        #no need to traverse the suffix link
                        if current.id == -1:
                            self.active_edge = ord(self.string[i - self.remaining + 1])
                            self.active_length -=1
                        #follow the trail of suffix link
                        #only change
                        if current.id is None:
                            self.active_node = current.suffix_link
                            
    def bwt(self):
        BWT = [None] * len(self.string)
        SA = self.traverse_bwt(self.root, [])

        for i in range(len(self.string)):
            BWT[i] = self.string[SA[i] - 1]
        return BWT
        
    def traverse_bwt(self, current, array):
        if current.isLeaf():
            array.append(current.id)
            
        for c in range(NUM_CHAR):
            if current.edge[c] is not None:
                current = current.child[c]
                self.traverse_bwt(current, array)
                current = current.parent
        return array
        
                    
                            
def main():
    s = []
    try:
        for line in open(sys.argv[1], 'r'):
            for c in line:
                s.append(str(c))
    except FileNotFoundError:
        print("File not found!")

        
    ST = SuffixTree(s)
    ST.construct()
    BWT = ST.bwt()
    f = open('output_bwt.txt', 'w')
    for i in range(len(BWT)):
        f.write(str(BWT[i]))
    f.close()

if __name__ == '__main__':
    main()
                      


















        
