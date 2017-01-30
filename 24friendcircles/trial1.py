# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:28:31 2017

@author: abgoswam
"""

class Vertex:
    def __init__(self, vid):
        self.vid = vid
        self.neighbors = set()
        self.visited = False
        
class Graph:
    def __init__(self, N):
        self.vertices = {}
        for i in range(N):
            self.vertices[i] = Vertex(i)
            
    def addEdge(self, vid_from, vid_to):
        self.vertices[vid_from].neighbors.add(vid_to)
        self.vertices[vid_to].neighbors.add(vid_from)

    def dfs(self, vid):
        v = self.vertices[vid]
        v.visited = True
#        print("vid (visited): {0}..".format(vid))
#        print("neighbors: {0}..".format(v.neighbors))
        for vid_neigh in v.neighbors:
#            print("vid_neigh : {0}..".format(vid_neigh))
            if self.vertices[vid_neigh].visited == False:
                self.dfs(vid_neigh)

    def numConnectedComponents(self):
        n = 0        
        for vid in self.vertices:
            v = self.vertices[vid]
            if v.visited == False:
                n += 1
                self.dfs(v.vid)
                
        return n

def  friendCircles(friends):
#    print(friends)
    g = Graph(len(friends))    
    
    for idx, friendpref in enumerate(friends):
    #    print(idx,  list(friendpref))
        for friendpref_idx, friendpref_pref in enumerate(friendpref):
    #        print(friendpref_idx, friendpref_pref)
            if idx == friendpref_idx:
                continue
            else:
                if 'Y' == friendpref_pref:
                    g.addEdge(idx, friendpref_idx)
                    
    print(g.numConnectedComponents())


_friends_cnt = int(raw_input().strip())
_friends_i = 0
_friends = []

while _friends_i < _friends_cnt:
    _friends_item = raw_input().strip()
    _friends.append(_friends_item)
    _friends_i += 1
    
print(_friends)
    
# ---------------
friends = _friends
g = Graph(len(friends))    

for idx, friendpref in enumerate(friends):
#    print(idx,  list(friendpref))
    for friendpref_idx, friendpref_pref in enumerate(friendpref):
#        print(friendpref_idx, friendpref_pref)
        if idx == friendpref_idx:
            continue
        else:
            if 'Y' == friendpref_pref:
                g.addEdge(idx, friendpref_idx)
                
print(g.numConnectedComponents())
    
    