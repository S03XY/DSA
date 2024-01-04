from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # mapping of graphs nodes

    def addEdges (self,u,v):
        self.graph[u].append(v)

if __name__== "__main__":
    g= Graph()
    



