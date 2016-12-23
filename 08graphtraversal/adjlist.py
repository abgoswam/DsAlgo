# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:51:32 2016

@author: abgoswam
"""

class Vertex:
    def __init__(self, vertexid):
        self.vid = vertexid
        self.visited = False # mark all nodes as unvisited
        self.adjacentidsweights = {}
      
    def addNeighbor(self, neighborid, weight = 0):
        self.adjacentidsweights[neighborid] = weight
      
class Graph:
    def __init__(self):
        self.numVertices = 0
        self.vidsVertex = {}
        return
        
    def addVertex(self, vertexid):
        self.numVertices = self.numVertices + 1
        self.vidsVertex[vertexid] = Vertex(vertexid)
        return
        
    def addEdge(self, frmid, toid, cost = 0):
        self.vidsVertex[frmid].addNeighbor(toid, cost)
        self.vidsVertex[toid].addNeighbor(frmid, cost) #since this is undirected
        return

    def displayGraph(self):
        for vid in self.vidsVertex:
            print "{0} -> ".format(vid),
            neighbors = self.vidsVertex[vid].adjacentidsweights
            for adjid in neighbors:
                print "{0}:{1}".format(adjid, neighbors[adjid]),

            print ""
        
    def dfs(self, vertexid):
        vertex = self.vidsVertex[vertexid]
        if vertex.visited is False:
            print ": {0}".format(vertex.vid),            
            vertex.visited = True    
            for adjid in vertex.adjacentidsweights:
                self.dfs(adjid)

        
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
#    g.addEdge('2','3',4)
    g.addEdge('4','1',2)
#    g.addEdge('4','3',4)

    print "Graph :"    
    g.displayGraph()
    
    print "DFS ",
    g.dfs('0')