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

    def DFSIterative (self,i):
        visted = [False for _ in range(max(g.graph)+1)]
        stack =[]

        stack.append(i)

        while stack:
            s = stack.pop()
            if (not visted[s]):
                print(s,end=" ")
                visted[s]= True

            for node in self.graph[s]:
                if not visted[node]:
                    stack.append(node)    

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
    g.DFSIterative(searchVertex)




# difference between depth first search and breadth first search 
# BFS is a vertex based technique which uses queue data structure, node is pushed into queue and the marked visited then adjacent node are appended to the queue at last and then marked visited and the next vertex is choosen from the queue and the process is repeated
    
# DFS is a edge based technique in which a node is pushed into  visited and the edges are appended into the stack, the next edge is choosen from the stack and all it adjacent node are pushed into the stack and this process is repeated until there are no more edges then the elements are popped from stack after the there is no more edges left