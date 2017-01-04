# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 14:03:10 2016

@author: abgoswam
"""

class Queue:
    def __init__(self):
        self.qdata = []
        
    def isEmpty(self):
        if len(self.qdata) <= 0:
            return True
        else:
            return False
        
    def enque(self, vid):
        self.qdata.append(vid)
        
    def deque(self):
        return self.qdata.pop(0)

class Vertex:
    def __init__(self, vid):
        self.vid = vid
        self.visited = False
        self.neighbors = {}
        
class Graph:
    def __init__(self):
        self.vertices = {}
        
    def addVertex(self, vid):
        v = Vertex(vid)
        self.vertices[vid] = v
        
    def addEdge(self, fromid, toid, weight):
        self.vertices[fromid].neighbors[toid] = weight
        self.vertices[toid].neighbors[fromid] = weight
        
    def dfs(self, vid):
        v = self.vertices[vid]
        v.visited = True
        print " .{0}".format(v.vid),
        for neighid in v.neighbors:
            if self.vertices[neighid].visited is False:            
                self.dfs(neighid)
        
    def bfs(self, vid):
        q = Queue()
        q.enque(vid)
        self.vertices[vid].visited = True
        
        while(q.isEmpty() == False):
            next_vid = q.deque()
            v = self.vertices[next_vid]
            print " .{0}".format(v.vid),

            for neighid in v.neighbors:
                if self.vertices[neighid].visited is False:
                    self.vertices[neighid].visited = True
                    q.enque(neighid)

        return True            
        
if __name__  == "__main__":
    g = Graph()
    
    g.addVertex('0')
    g.addVertex('1')
    g.addVertex('2')
    g.addVertex('3')
    
    g.addEdge('0', '1', 10)
    g.addEdge('0', '2', 10)
    g.addEdge('1', '3', 10)
    g.addEdge('2', '3', 10)
    
#    print "DFS:", 
#    g.dfs('0')
    
    print "BFS:", 
    g.bfs('0')
#    print 