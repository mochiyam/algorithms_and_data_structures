from AdjList import Vertex, AdjList

class Graph:
    '''
-Creates an object Graph: undirected graph that consists adjacent list
of vertices and edges
-Applied Adjacency List
'''
    def __init__(self, V = None, E = None):
        self.vertex = AdjList()
        self.edge = AdjList()
        self.max_vertex = 0
        self.countEdge = 0
        
    def addEdge(self, u, v, w):
        self.addVertices(u)
        self.addVertices(v)
        self.edge.insert([w, u, v])
        self.countEdge += 1

    def addVertices(self, x):
        if x > self.max_vertex:
            self.max_vertex = x
        if not self.vertex.contains(x):
            self.vertex.insert(x)

    def getVertex(self):
        return self.vertex.item

    def getEdge(self):
        return self.edge.item

    def getArrayEdge(self):
        '''
This function returns adjacency list into an array.
Auxilary Space Complexity: O(E)
'''
        E = [None] * len(self.edge)
        i = 0
        current_edge = self.edge.head
        while current_edge is not None:
            E[i] = current_edge.item
            current_edge = current_edge.next
            i+=1
        return E
