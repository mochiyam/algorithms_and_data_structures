#global variable
NUM_CHAR = 256

class Node:
    
    def __init__(self, id = None, parent = None):
        self.id = id
        self.edge = [None]*NUM_CHAR
        self.child = [None]*NUM_CHAR
        self.parent = parent
        self.suffix_link = None
        
    def isLeaf(self):
        return self.id is not None and self.id != -1
    
    def addSuffixLink(self, node):
        self.suffix_link = node

class Edge:
    def __init__(self, start = None, end = None):
        self.start = start
        self.end = end

    def setEdge(self, start, end):
        self.start = start
        self.end = end

    def getStartEnd(self):
        return self.start, self.end

    def getDepth(self):
        return self.end - self.start + 1

class SuffixTree:
    def __init__(self, string):
        self.root = Node(-1)
        self.root.parent = self.root
        self.string = string
        self.global_end = 0

        self.active_position = -1

    def splitEdge(self, index, current, internal_node, new_leaf, x, new):
        #set a new parent for the current child
        child = current.child[index]
        child.parent = internal_node

        #internal node have 2 children
        internal_node.child[ord(self.string[x])] = child
        internal_node.edge[ord(self.string[x])] = Edge(x, self.global_end)        

        internal_node.child[ord(self.string[new])] = new_leaf
        internal_node.edge[ord(self.string[new])] = Edge(new, self.global_end)

        internal_node.addSuffixLink(current)
    
        #parent points to internal node (new child)
        current.child[index] = internal_node
        current.edge[index].setEdge(current.edge[index].start, x-1)

        return internal_node
    
    def traverse(self, current, index, length, j):
        print('length: ' + str(length))
        print(current.id)
        print(index)
        #if current[index] is None
        if current.child[index] is None:
            print('index does not exist')
            return current, -1
        #if it ends at leaf
        elif current.child[index].isLeaf():
        #if str[i] ends within the edge label : Rule 3
            print('length: ' + str(length))
            print('depth: ' + str(current.edge[index].getDepth()))
            print('start: ' + str(current.edge[index].start))
            print('end: ' + str(current.edge[index].end))
            print('id:' + str(current.id))
            if current.edge[index].getDepth() > length:
                print('Rule 3')
                position = current.edge[index].start + length
                print('position: ' + str(position))
                return current, position
            else:
                print('ends at leaf')
                return current.child[index], current.edge[index].start
        else:
            if current.edge[index] is not None:
                depth = current.edge[index].getDepth()
                print('get depth: ' + str(current.edge[index].getDepth()))
                start = current.edge[index].start
                print('start: ' + str(start))
                new_index = ord(self.string[j + depth])
                #if current.child
                print(chr(index))
                return self.traverse(current.child[index], new_index, length - depth, j)            
        
    def construct(self):
        n  = len(self.string)
        current = self.root

        #construct implicitST_0
        leaf = Node(0, current)
        current.child[ord(self.string[0])] = leaf
        current.edge[ord(self.string[0])] = Edge(0, self.global_end)
        print(ord(self.string[0]))
        
        i = 0
        while i <n-1:
            j = 0
            ptr = self.root
            self.global_end = i + 1
            while j <= (i + 1):
                index = ord(self.string[j])
                print('i: ' + str(i))
                print('j: ' + str(j))
                print('index: ' + str(index) + '  string: ' + str(self.string[j]))
                print('current position: ' + str(current.id))
                
                #locate string[j...i]
                #Extension 1
                if j == 0:
                    current, position = self.traverse(current, index , abs(i-j) + 1, j)
                else:
                    #Extension >= 2
                    #walk up exactly one edge
                    current = current.parent
                    print('walk up one edge: ' + str(current.id))
                    if current.id != -1:
                        #substring corresponding to that edge str[position_k...i]
                        #position_k = current.edge[i - 
                        #follow its suffix link
                        current = current.suffix_link
                        print('suffix link: ' + str(current.id))
                        #walk down along the path
                        print(self.active_position)
                        if current.id is not None:
                            current, position = self.traverse(current, index, abs(i- j + 1), j)
                        else:
                            current, position = self.traverse(current, ord(self.string[self.active_position]), abs(i-self.active_position)+ 1, j)
                    else:   
                        current, position = self.traverse(current, index, abs(i-j) + 1, j)

                    if current.id is None:
                       self.active_position = position
                print('position: ' + str(position))
                print('located position: ' + str(current.id))            
                #apply pertinent suffix extension rule for str[i + 1]
                #Rule 1:
                if current.isLeaf():
                    current.parent.edge[ord(self.string[position])].end = self.global_end
                    print('Rule 1: ')
                    for k in range(j, i+2, 1):
                        print(str(self.string[k]), end = ' ' )
                        
                #is current.edge[index] does not exist
                elif position == -1:
                    current.child[index] = Node(j, current)
                    current.edge[index] = Edge(j, self.global_end)
                    print('leaf created! ' + str(self.string[j]))
                else:
                # it means that it did not end in leaf
                    #Rule 2
                    if self.string[position] != self.string[i+1]:
                        print('Rule 2: ')
                        if self.string[i+1] != self.string[position]:
                            print('new leaf created: ' + str(j))
                            for m in range(i+1, i+2, 1):
                                print(str(self.string[m]), end = ' ' )
                            print('\ninternal node to leaf: ')
                            for p in range(position, i+2, 1):
                                print(str(self.string[p]), end = ' ' )
                            print('\n')
                            
                            #create a new leaf and internal node
                            internal_node = Node(None, current)
                            new_leaf = Node(j, internal_node)

                            current = self.splitEdge(index, current, internal_node, new_leaf, position, i+1)
                            self.active_position = position
                            if ptr != self.root:
                                ptr.addSuffixLink(current)
                            ptr = current
                            print('current ' + str(current.id) + str(current.edge[ord(self.string[i+1])].start) + str(current.edge[ord(self.string[i+1])].end))
                            print(self.string[i+1])
                j+=1
                print('\n')
            i+=1
    def bwt(self):
        BWT = [None] * len(self.string)
        SA = self.bwt_traverse(self.root, [])
        print(SA)
        for i in range(len(self.string)):
            BWT[i] = self.string[SA[i] - 1]
        print(BWT)
        
    def bwt_traverse(self, current, array):
        if current.isLeaf():
            print('current id: ' + str(current.id))
            array.append(current.id)
            print(array)
        for c in range(NUM_CHAR):
            if current.edge[c] is not None:
                for i in range(current.edge[c].start, current.edge[c].end + 1, 1):
                    print(str(self.string[i]), end = ' ' )
                current = current.child[c]
                print('\n')
                self.bwt_traverse(current, array)
                current = current.parent
        return array
                            
def main():
    #s = 'suffix_trees_and_bwt_are_related$'
    s = 'abccabx$'
    ST = SuffixTree(s)
    ST.construct()
    ST.bwt()
    
    
if __name__ == '__main__':
    main()
    

                      


















        
