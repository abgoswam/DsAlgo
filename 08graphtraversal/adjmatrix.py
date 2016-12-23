# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:32:23 2016

@author: abgoswam
"""

from tabulate import tabulate

#class Vertex:
#    def __init__(self, node):
#        self.id = node
#        self.visited = False # mark all nodes as unvisited
        
    
class Graph:
    def __init__(self, numVertices, cost = 0):
        
        self.numVertices = numVertices
        self.adjMatrix = [[0] * numVertices for _ in range(numVertices)]
        self.visited = [False for _ in range(numVertices)]
        
#        self.vertices = []
#        for i in range(numVertices):
#            newVertex = Vertex(i)
#            self.vertices.append(newVertex)
            
    def dfs(self, vid):            
        if self.visited[vid] is False:
            print " {0}".format(vid),
            self.visited[vid] = True
            for i in range(self.numVertices):
                if self.adjMatrix[vid][i] == 1:
                    self.dfs(i)
      
      
if __name__ == "__main__":
    g = Graph(5)
    print tabulate(g.adjMatrix)
    
    g.adjMatrix[0][1] = g.adjMatrix[1][0] = 1
    g.adjMatrix[0][2] = g.adjMatrix[2][0] = 1
    g.adjMatrix[1][2] = g.adjMatrix[2][1] = 1
    g.adjMatrix[1][4] = g.adjMatrix[4][1] = 1
#    g.adjMatrix[2][3] = g.adjMatrix[3][2] = 1
#    g.adjMatrix[3][4] = g.adjMatrix[4][3] = 1
    
    print tabulate(g.adjMatrix)
    
    print "DFS : ",
    g.dfs(3)
    