from collections import defaultdict

# in breadth-first search there are two things to consider visited and queue 
"""
    first put data inside the queue and then push inside the visited 
    pop the queue from start index and visit all it neighbors and if push in the queue 
    if the neighbor is not visited
    when the queues is empty exit the loops
    
"""



# * Graph representation using adjacency list
class Graph:

    def __init__(self):
        self.graph =defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False] *(max(self.graph)+1)
        queue = []


        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop()
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i] is False:
                    visited[i] = True
                    queue.append(i)




if __name__ == "__main__":

    g= Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)


    print(f"graph is {g.graph}")

    searchIndex = 2
    g.BFS(searchIndex)


