#global variable
NUM_CHAR = 256

class Node:
    
    def __init__(self, id = None, parent = None):
        self.id = id
        self.edge = [None]*NUM_CHAR
        self.child = [None]*NUM_CHAR
        self.parent = parent
        self.link = None
        
    def isLeaf(self):
        return self.id is not None
    
    def getChild(self, x):
        if self.child[x] is not None:
            return self.child[x]
        else:
            return None

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
        self.root = Node()
        self.string = string
        self.global_end = 0

    def splitEdge(self, index, current, internal_node, new_leaf, x, i ):
        #set new parent for the current child
        child = current.getChild(index)
        child.parent = internal_node

        #internal node have 2 children
        internal_node.child[ord(self.string[x])] = child
        internal_node.edge[ord(self.string[x])] = Edge(x, self.global_end)

        internal_node.child[ord(self.string[i])] = new_leaf
        internal_node.edge[ord(self.string[i])] = Edge(i, self.global_end)
    
        #parent points to internal node (new child)
        current.child[index] = internal_node
        current.edge[index].setEdge(current.edge[index].start, x-1)
        
    def find_depth(self, current, index, i, j, depth):
        print('start ' + str(current.edge[index].start))
        print('end ' + str(current.edge[index].end))
        if current.child[index].isLeaf():
            depth += current.edge[index].getDepth()
            print('start ' + str(current.edge[index].start))
            print('end ' + str(current.edge[index].end))
            print('End traverse depth: ' + str(depth))
            return depth, current, index
        else:
            depth += current.edge[index].getDepth()
            current = current.child[index]  
            index = ord(self.string[j + depth])        
            print("string " + str(self.string[j + depth]))
            print('Traverse depth: ' + str(depth))
            return self.find_depth(current, index, i, j, depth)
            
            '''
            try:
                depth += current.edge[index].getDepth()
                current = current.child[index]
                #Rule 3
                if j + depth > i:
                    return depth, current, index
                index = ord(self.string[j + depth])
                #Rule 1
                if current.edge[index] is None:
                    current.child[index] = Node(j, current)
                    current.edge[index] = Edge(i, self.global_end)
                    print('leaf created! ' + str(self.string[j]))
                    return depth, current, index
                print("string " + str(self.string[j + depth]))
                print('Traverse depth: ' + str(depth))
                return self.find_depth(current, index, i, j, depth)
            except IndexError:
                return depth - j, current.parent, index
                '''
    def construct(self):
        n  = len(self.string)

        for i in range(n):
            j = 0
            self.global_end = i
            while j <= i:
                current = self.root
                print('i: ' + str(i))
                print('j: ' + str(j))
                index = ord(self.string[j])
                print('index: ' + str(index) + '  string: ' + str(self.string[j]))
                
                index = ord(self.string[j])
                if current.child[index] is not None:
                    x = current.edge[index].start + (i - j)
                    depth, current, index = self.find_depth(current, index, i, j, 0)
                    print('depth: ' + str(depth))
                    #Rule 1
                    if depth == (i-j):
                        print('depth: ' + str(current.edge[index].getDepth()))
                        print('self.global_end: ' + str(self.global_end))
                        print(current.edge[index].start)
                        current.edge[index].setEdge(current.edge[index].start, self.global_end)
                        print('Rule 1: ')
                        for i in range(j, i+1, 1):
                            print(str(self.string[i]), end = ' ' )
                    #Rule 2
                    else: 
                        print('Rule 2: ')
                        if self.string[i] != self.string[x]:
                            print('new leaf created: ' + str(j))
                            for i in range(i, i+1, 1):
                                print(str(self.string[i]), end = ' ' )
                            print('\ninternal node to leaf: ')
                            for i in range(x, i+1, 1):
                                print(str(self.string[i]), end = ' ' )

                            #create a new leaf and internal node
                            internal_node = Node(None, current)
                            new_leaf = Node(j, internal_node)
                            
                            self.splitEdge(index, current, internal_node, new_leaf, x, i)

                else:
                    current.child[index] = Node(j, current)
                    current.edge[index] = Edge(i, self.global_end)
                    print('leaf created! ' + str(self.string[j]))

                j+=1
                print('\n')
                
    def bwt(self):
        BWT = [None] * len(self.string)
        SA = self.traverse(self.root, [])
        print(SA)
        for i in range(len(self.string)):
            BWT[i] = self.string[SA[i] - 1]
        print(BWT)
        
    def traverse(self, current, array):
        if current.isLeaf():
            print('current id: ' + str(current.id))
            array.append(current.id)
            print(array)
        for c in range(NUM_CHAR):
            if current.edge[c] is not None:
                for i in range(current.edge[c].start, current.edge[c].end+1, 1):
                    print(str(self.string[i]), end = ' ' )
                current = current.child[c]
                print('\n')
                self.traverse(current, array)
                current = current.parent
        return array
        
                    
                            
def main():
    s = 'suffix_trees_and_bwt_are_related$'
    #s = 'abcabx$'
    ST = SuffixTree(s)
    ST.construct()
    ST.bwt()
    
    
if __name__ == '__main__':
    main()
    

                      


















        
