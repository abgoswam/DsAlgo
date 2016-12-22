# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:32:23 2016

@author: abgoswam
"""

class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False # mark all nodes as unvisited
        
    
class Graph:
    def __init__(self, numVertices, cost = 0):
        
        self.numVertices = numVertices
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        
#        self.vertices = []
        
#        for i in range(numVertices):
#            newVertex = Vertex(i)
#            self.vertices.append(newVertex)
            
if __name__ == "__main__":
    g = Graph(5)
    print g.adjMatrix