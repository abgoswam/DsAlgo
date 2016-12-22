# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:51:32 2016

@author: abgoswam
"""

class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False # mark all nodes as unvisited
        self.adjacent = {}
      
    def addNeighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight
      
class Graph:
    def __init__(self):
        self.numVertices = 0
        self.vertexDictionary = {}
        return
        
    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertexDictionary[node] = newVertex
        return
        
    def addEdge(self, frm, to, cost = 0):
        self.vertexDictionary[frm].addNeighbor(to, cost)
        self.vertexDictionary[to].addNeighbor(frm, cost) #since this is undirected
        return
        
if __name__ == "__main__":
    g = Graph()
    
    g.addVertex('0')
    g.addVertex('1')
    g.addVertex('2')
    g.addVertex('3')
    g.addVertex('4')
    
    g.addEdge('0','1',4)
    g.addEdge('0','2',1)
    g.addEdge('2','1',2)
    g.addEdge('2','3',4)
    g.addEdge('4','1',2)
    g.addEdge('4','3',4)
    