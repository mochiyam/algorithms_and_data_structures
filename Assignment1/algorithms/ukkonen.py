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
    def __init__(self, string, global_end = 0):
        self.root = Node()
        self.string = string
        '''

    def traverse(self, index):
        count = 0
        traverse_aux(self.root, index, count)
        
    def traverse_aux(self, current, index):
        count += current.edge[index].getDepth()
            if 
            return self.traverse(current.child[index], index + count)
            '''
    def construct(self):
        n  = len(self.string)

        for i in range(n):
            j = 0
            current = self.root
            
            while j<= i:
                print('i: ' + str(i))
                print('j: ' + str(j))
                index = ord(self.string[j])
                print('index: ' + str(index) + '  string: ' + str(self.string[j]))
                
                index = ord(self.string[j])
                if current.child[index] is not None:
                    #Rule 1
                    if current.edge[index].getDepth() == (i-j):
                        print('depth: ' + str(current.edge[index].getDepth()))
                        current.edge[index].setEdge(j, i)
                        print('Rule 1: ')
                        for i in range(j, i+1, 1):
                            print(str(self.string[i]), end = ' ' )
                    #Rule 2
                    else:
                        #Trick 1
                        count = 0
                        while current.edge[index].getDepth() < (i-j):
                            count += current.edge[index].getDepth()
                            if current.child[index].isLeaf():
                                break
                            current = current.child[index]
                            index = ord(self.string[j+count])
                            print(index)
                        print('Rule 2: ')
                        x = current.edge[index].start + (i - j)
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
                            #child points to the new parent: internal node
                            child = current.getChild(index)
                            child.parent = internal_node
                            #internal node have 2 children
                            internal_node.child[x] = child
                            internal_node.edge[x] = Edge(x, i)

                            internal_node.child[i] = new_leaf
                            internal_node.edge[i] = Edge(j + 1, i)

                            current.child[index] = internal_node
                            current.edge[index].setEdge(current.edge[index].start, x-1)
                            
                            
                            
                        
                else:
                    current.child[index] = Node(j, current)
                    current.edge[index] = Edge(i, j)
                    print('leaf created! ' + str(self.string[j]))

                j+=1
                print('\n')
                    
                            
def main():
    s = 'abba$'
    ST = SuffixTree(s)
    ST.construct()
    #ST.print()
    
    
if __name__ == '__main__':
    main()
    

                      


















        
