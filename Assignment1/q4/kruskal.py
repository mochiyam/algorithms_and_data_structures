import sys
from AdjList import AdjList
from Graph import Graph
from Quicksort import quicksort

class UnionByRank:
    '''
-This class computes union-by-rank using path compression
-Initializes the parrent array corresponding to the root element of disjoint set
-The root of the set stores the height of the tree
'''
    def __init__(self, N):
        self.parent = [None] * N
        for i in range(N):
            self.makeDisjointSet(i)

    def makeDisjointSet(self, x):
        #storing as height + 1
        self.parent[x] = -1

    def find(self, a):
        '''
-This function will find the root of the disjoint set
-Path compression is performed
-Applied recursive function
Time Complexity: O(log(V))
'''
        if self.parent[a] < 0:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
                                   
    def union(self, a, b):
        '''
-This function will merge two disjoint subset containing
a and b in disjoint set
Time Complexity: O(1)
'''
        root_a = self.find(a)
        root_b = self.find(b)
        #if a and b are in the same tree
        if (root_a == root_b):
            return
        #height of the tree contains a
        height_a = -self.parent[root_a]
        #height of the tree contains b
        height_b = -self.parent[root_b]
        if(height_a > height_b):
            self.parent[root_b] = root_a
        elif (height_b > height_a):
            self.parent[root_a] = root_b
        #if height_a = height_b
        else:
            self.parent[root_a] = root_b
            self.parent[root_b] = -(height_b + 1)
            
def kruskal(graph):
'''
-This function computes Kruskal's algorithm.
-Greedy function
:pre-condition: a graph object is created
:post-condition: a linked list of minimum spanning tree (MST) will be returned
Time Complexity: O(E*log(V))
'''
    current = graph.vertex.head
    length_vertex = graph.max_vertex + 1
    E= graph.getArrayEdge()
    #sort the edges using quicksort: O(E*log(E))
    quicksort(E, 0, len(E)-1)
    UnionFind = UnionByRank(length_vertex)
    MST = AdjList()
    #Apply Union-Find disjoing set data structure for each edge: O(E*log(V))
    for edge in E:
        u = edge[1]
        v = edge[2]
        w = edge[0]
        if UnionFind.find(u) != UnionFind.find(v):
            UnionFind.union(u, v)
            MST.insert([u, v, w])
    return MST

def main():
    g = Graph()
    try:
        for line in open((sys.argv[1], 'r')):
            x = line.strip("\n")
            g.addEdge(int(x.split(" ")[0]), int(x.split(" ")[1]), int(x.split(" ")[2]))
    except FileNotFoundError:
        print("File not found!")
        
    MST = kruskal(g)
    f = open('output_kruscal.txt', 'w')
    current = MST.head
    while current is not None:
        for i in range(3):
            f.write(str(current.item[i]) + ' ')
        f.write("\n")
        current = current.next
    f.close()
    
if __name__ == '__main__':
    main()
    g = Graph()
    '''
    try:
        for line in (open('test.txt', 'r')):
            x = line.strip("\n")
            g.addEdge(int(x.split(" ")[0]), int(x.split(" ")[1]), int(x.split(" ")[2]))
    except FileNotFoundError:
        print("File not found!")
'''
