#global variable
NUM_CHAR = 256
global_end = -1

class Node:
    
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
    def __init__(self, start = None, end = None):
        self.start = start
        self.end = end

    def setEdge(self, start, end):
        self.start = start
        self.end = end

    def getStartEnd(self):
        return self.start, self.end

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
        print('position: ' + str(internal_node.edge[ord(self.string[position])].start))
        for i in range(position, global_end+1, 1):
            print(str(self.string[i]), end = ' ' )
        print('    ')
        internal_node.child[index] = new_leaf
        internal_node.edge[index] = Edge(i, global_end)
        for i in range(i, global_end+1, 1):
            print(str(self.string[i]))

        internal_node.suffix_link = self.root
        #parent points to internal node (new child)
        current.child[self.active_edge] = internal_node
        current.edge[self.active_edge].setEdge(current.edge[self.active_edge].start, position-1)

    def traverse(self):
        length = self.active_node.getDepth(self.active_edge)
        print(self.active_edge)
        print('length: ' + str(length) + ' active_length ' + str(self.active_length))
        return self.traverse_aux(self.active_node, length)
            
    def traverse_aux(self, current, length):
        if length >= self.active_length:
            return self.activePoint() #position              
        elif length < self.active_length:
            self.active_node = self.active_node.child[self.active_edge]
            length += self.active_length
            self.active_edge = ord(self.string[length])
            self.traverse_aux(self.active_node, length)                
  
    def construct(self):
        n  = len(self.string)

        for i in range(n):
            print('i: ' + str(i))
            for i in range(0, i+1, 1):
                print(str(self.string[i]), end = ' ' )
            global global_end
            global_end = i
            index = ord(self.string[i])
            self.remaining += 1
            self.new_internal_node = None

            while(self.remaining > 0):
                current = self.active_node
                print('\nremaining: ' + str(self.remaining))
                for c in range(NUM_CHAR):
                    if current.child[c] is not None:
                        print('char: ' + str(chr(c)))

                #There are no active edge coming from the active node
                if self.active_length == 0:                  
                    #Rule 2: create a new leaf
                    if current.child[index] is None:
                        current.child[index] = Node(i - self.remaining + 1, current)
                        current.edge[index] = Edge(i, global_end)
                        #self.active_edge = ord(self.string[i - self.remaining + 1])
                        self.remaining -= 1
                        print('leaf created! ' + str(self.string[i]))
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
                    '''if current.getDepth(self.active_edge) >= self.active_length:
                        position = self.activePoint()
                        print('position: '+ str(position) + ' ' + str(self.string[position]))
                        '''
                    print('current depth: ' + str(current.getDepth(self.active_edge)))
                    print('char_index: ' + str(self.string[position]))
                    print('index: ' + str(chr(index)))
                    char_index = ord(self.string[position])
                    #Rule 3
                    if char_index == index:
                        self.active_length += 1
                        print('active length: ' + str(self.active_length))
                        if current.getDepth(self.active_edge) == self.active_length:
                            self.active_node = current.child[self.active_edge]
                            self.active_edge = -1
                            self.active_length = 0
                        #Trick 3: premature extension stopping criterion
                        break
                    else: #if char_index != index
                        internal_node = Node(None, current)
                        new_leaf = Node(i - self.remaining + 1, internal_node)
                        #new_leaf = Node(i, internal_node)
                        print('create an internal node! ' + str(self.string[i]))
                        self.splitEdge(internal_node, current, new_leaf, char_index, index, position, i)
                        self.remaining -= 1
                        if self.new_internal_node is not None:
                            print('internal node')
                            self.new_internal_node.suffix_link = internal_node
                        self.new_internal_node = internal_node
                        #if active node is at the root
                        #no need to traverse the suffix link
                        if current.id == -1:
                            print('at the root!')
                            self.active_edge = ord(self.string[i - self.remaining + 1])
                            self.active_length -=1
                        #follow the trail of suffix link
                        #only change
                        if current.id is None:
                            self.active_node = current.suffix_link
                            print('internal node!')
                            
                    print('active point: (' + str(self.active_node.id) + ', ' + str(chr(self.active_edge)) + ', ' + str(self.active_length) + ')')
            print('active node: ' + str(self.active_node.id))
            print('active edge: ' + str(self.active_edge))
            print('active length: ' + str(self.active_length))
                
            print('\n')
    def bwt(self):
        BWT = [None] * len(self.string)
        SA = self.traverse_bwt(self.root, [])
        print(len(BWT))
        print(len(SA))
        print(SA)
        for i in range(len(self.string)):
            BWT[i] = self.string[SA[i] - 1]
        print(BWT)
        
    def traverse_bwt(self, current, array):
        if current.isLeaf():
            print('current id: ' + str(current.id))
            array.append(current.id)
            print(str(array) + '\n')
        for c in range(NUM_CHAR):
            if current.edge[c] is not None:
                print('char: ' + str(chr(c)))
                for i in range(current.edge[c].start, current.edge[c].end+1, 1):
                    print(str(self.string[i]), end = ' ' )
                current = current.child[c]
                self.traverse_bwt(current, array)
                current = current.parent
        return array
        
                    
                            
def main():
    #s = 'trees_and_bwt_are_$'
    s = 'suffix_trees_and_bwt_are_related$'
    #s = 'abcabxabcd$'
    ST = SuffixTree(s)
    ST.construct()
    ST.bwt()
    
    
if __name__ == '__main__':
    main()
    

                      


















        
