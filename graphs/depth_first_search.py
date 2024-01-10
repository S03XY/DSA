# this graph is represented via adjacency list
# in DFS the new edges are stored at front in stacked edge list

""" 
    concept-> 
        have two array one for the visted node and one for the stacked edges
        then push the node to visted and put the edges into stacked array in the front not in at the last 
        remove it first stacked edge and see all its neighbour untill no nodes have any more edges left
"""



from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSRecursion(self,i,visited:set):
        visited.add(i)
        print(i,end=" ")
        for neighbor in self.graph[i]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.DFSRecursion(neighbor,visited)

    def DFS(self,i):
        visited = set()
        self.DFSRecursion(i,visited)



if __name__ == "__main__":
    g= Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    print(f"graph constructed {g.graph}")

    searchVertex = 2

    print(f"Starting depth first search from index {searchVertex}")

    g.DFS(searchVertex)






