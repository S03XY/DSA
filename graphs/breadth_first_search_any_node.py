from collections import defaultdict

# Graph represented using adjacency list

class GraphNode:

    def __init__ (self,id,name):
        self.id = id
        self.name = name

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u.id].append(v)


    def BFS(self,node):

        visited = defaultdict(bool)
        queue = []    
        queue.append(node)
        visited[node.id] = True

        while queue:
            node = queue.pop()
            print(node.id,end=" ")

            for i in self.graph[node.id]:
                if visited[i.id] is False:
                    visited[i.id] = True
                    queue.append(i)



if  __name__ == "__main__":

    g = Graph()

    node0 = GraphNode(0,"shashank")
    node1 = GraphNode(1,"rohan")
    node2 = GraphNode(2,"prasant")
    node3 = GraphNode(3,"rohini")
    
    

    g.addEdge(node0,node1)
    g.addEdge(node0,node2)
    g.addEdge(node1,node2)
    g.addEdge(node2,node0)
    g.addEdge(node2,node3)
    g.addEdge(node3,node3)


    print(f"resulting graph {g.graph}")

    searchIndex = node2
    g.BFS(node2)






