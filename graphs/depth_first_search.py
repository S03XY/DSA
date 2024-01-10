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

    def DFSRecursion(self,nodeIndex,visited:set):
        visited.add(nodeIndex)
        print(nodeIndex,end=" ")    

        for neighbor in self.graph[nodeIndex]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.DFSRecursion(neighbor,visited)
        

    def DFS(self,nodeIndex):
        visted =set()
        self.DFSRecursion(nodeIndex,visted)    

    def DFSNormal (self,i):
        visted = [False for _ in range(max(g.graph)+1)]
        stack =[]

        visted[i] = True
        stack.insert(0,i)

        print(f"stack {stack}")

        while stack:
            poppedItem = stack.pop(0)
            print(poppedItem,end=" ")

            for neighbor in g.graph[poppedItem]:
                if visted[neighbor] == False:
                    visted[neighbor] = True
                    stack.insert(0,neighbor)




            


if __name__ == "__main__":
    g= Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    searchVertex = 2

    print(f"graph constructed {g.graph}")
    # print(f"Starting depth first search from index {searchVertex}")

    g.DFS(searchVertex)
    print("")
    g.DFSNormal(searchVertex)






